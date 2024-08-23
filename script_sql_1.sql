CREATE VIEW V_NPS_DERIVADO AS 
WITH nps_grouped AS (
    SELECT n.case_id,
           CASE 
               WHEN n.nps_score >= 0 AND n.nps_score <= 6 THEN -1
               WHEN n.nps_score >= 7 AND n.nps_score <= 8 THEN 0
               WHEN n.nps_score >= 9 AND n.nps_score <= 10 THEN 1
           END AS nps_group
    FROM public.nps n
),
case_categories AS (
    SELECT DISTINCT i.case_id,
           CASE 
               WHEN i.interaction_type = 'rep_derivation' THEN 'derivado'
               ELSE 'no_derivado'
           END AS referral_status
    FROM public.interacciones i
),
nps_by_category AS (
    SELECT 
        cc.referral_status,
        COUNT(CASE WHEN ng.nps_group = 1 THEN 1 END) AS count_promoters,
        COUNT(CASE WHEN ng.nps_group = -1 THEN 1 END) AS count_detractors,
        COUNT(*) AS count_total
    FROM case_categories cc
    LEFT JOIN nps_grouped ng ON cc.case_id = ng.case_id
    GROUP BY cc.referral_status
)
SELECT 
    referral_status,
    (count_promoters - count_detractors) * 1.0 / count_total AS nps
FROM nps_by_category;

