
CREATE TABLE fact_nav (
    amfi_code INTEGER,
    date TEXT,
    nav REAL
);
CREATE TABLE fact_transactions (
    transaction_id INTEGER,
    amfi_code INTEGER,
    investor_id INTEGER,
    transaction_type TEXT,
    amount REAL,
    date TEXT
);


CREATE TABLE fact_performance (
    amfi_code INTEGER,
    return_1m REAL,
    return_6m REAL,
    return_1y REAL
);