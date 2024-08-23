CREATE TABLE public.nps (
    survey_id SERIAL PRIMARY KEY,
    case_id VARCHAR(10) NOT NULL,
    nps_score INTEGER CHECK (nps_score BETWEEN 0 AND 10),
    ps_comment TEXT
);

