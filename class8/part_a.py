# Part A
#
# Count the total number of characters in all the tokens.
#
# Fill in the while loop below. Do not change anything else.

from prompt_tokens import PromptTokens

source = PromptTokens(["I", "reside", "in", "Delhi", "."])
total = 0

# ---- WRITE ONLY THIS WHILE LOOP ----
while source.has_next():
    tok = source.next_token()
    total = total + len(tok)

# ------------------------------------

print(total)