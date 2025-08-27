
'''

RunnableSequence is a LangChain primitive that lets you compose multiple steps into a pipeline.
Each step is a Runnable, and the output of one step becomes the input to the next. 
Think of it as a functional chain — like Unix pipes or RxJS observables.


'''

from langchain_core.runnables import RunnableLambda, RunnableSequence

# Step 1: Convert to uppercase
to_upper = RunnableLambda(lambda x: x.upper())

# Step 2: Append suffix
add_suffix = RunnableLambda(lambda x: f"{x} - processed")

# Compose the sequence
pipeline = RunnableSequence(first=to_upper, last=add_suffix)

# Run it
result = pipeline.invoke("hello world")
print(result)  # Output: "HELLO WORLD - processed"


### ------------------------------------------------------------------------------------------


from langchain_core.runnables import RunnableLambda, RunnableSequence

# Step 1: Check age eligibility
def check_age(applicant):
    if applicant["age"] >= 21:
        return applicant
    raise ValueError("Loan rejected: Age must be 21+")

# Step 2: Check required documents
def check_documents(applicant):
    required = {"id_proof", "income_proof"}
    submitted = set(applicant["documents"])
    if required.issubset(submitted):
        return applicant
    raise ValueError("Loan rejected: Missing required documents")

# Step 3: Verify documents
def verify_documents(applicant):
    # Simulate verification logic
    if applicant.get("documents_verified", False):
        return applicant
    raise ValueError("Loan rejected: Documents not verified")

# Step 4: Final approval
def approve_loan(applicant):
    return {"status": "Approved", "applicant": applicant["name"]}

# Compose sequence
loan_pipeline = RunnableSequence(
    first=RunnableLambda(check_age),
    middle=[
        RunnableLambda(check_documents),
        RunnableLambda(verify_documents)
    ],
    last=RunnableLambda(approve_loan)
)

# Sample input
applicant = {
    "name": "Ravi",
    "age": 30,
    "documents": ["id_proof", "income_proof"],
    "documents_verified": True
}

result = loan_pipeline.invoke(applicant)
print(result)

###----------------

from langchain_core.runnables import RunnableMap

doc_checks = RunnableMap({
    "id_check": RunnableLambda(lambda x: "id_proof" in x["documents"]),
    "income_check": RunnableLambda(lambda x: "income_proof" in x["documents"]),
    "address_check": RunnableLambda(lambda x: "address_proof" in x["documents"])
})

doc_result = doc_checks.invoke(applicant)
print(doc_result)

##------------------------------------------------------------------------------------------

from langchain_core.runnables import RunnableBranch

approve = RunnableLambda(lambda x: {"status": "Approved", "name": x["name"]})
reject = RunnableLambda(lambda x: {"status": "Rejected", "reason": "Verification failed"})

branch = RunnableBranch(
    (lambda x: x.get("documents_verified", False), approve),
    default=reject
)

result = branch.invoke(applicant)
print(result)
