from pydantic import BaseModel

class LoanRequest(BaseModel):

    loan_amnt: float
    term: str
    int_rate: float
    installment: float
    annual_inc: float
    dti: float
    emp_length: str
    home_ownership: str
    purpose: str
    fico_range_low: int
    fico_range_high: int
    open_acc: int
    pub_rec: int
    revol_bal: float
    revol_util: float
    mort_acc: float
    grade: str
    sub_grade: str
    verification_status: str
    inq_last_6mths: int
    delinq_2yrs: int