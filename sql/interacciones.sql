CREATE TABLE public.interacciones (
    case_id INTEGER PRIMARY KEY,
    interaction_id VARCHAR(10) NOT NULL,
    interaction_type VARCHAR(20) NOT NULL,
    representante VARCHAR(50),
    int_date DATE NOT NULL,
    FOREIGN KEY (representante) REFERENCES public.representantes(representante)
);

