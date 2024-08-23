CREATE TABLE public.representantes (
    representante VARCHAR(50) PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    team INTEGER NOT NULL,
    incoming_date DATE NOT NULL,
    status VARCHAR(10) CHECK (status IN ('Active', 'Inactive'))
);

