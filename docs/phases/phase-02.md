# Phase 2: Ad brief (LLM)

| Step | Build | Test and pass | Watch for |
|---|---|---|---|
| 2a | LLM adapter with one provider (Gemini free) | Returns text for a test prompt | Rate limits |
| 2b | Retry with backoff, plus a second provider (Groq) as fallback | Fallback triggers when the first is blocked on purpose | Different output style per model |
| 2c | Prompt that produces the brief: hook, 3 benefits, tone, CTA, scene list | Readable brief for all 10 products | Generic wording |
| 2d | Force strict JSON and validate with pydantic | 30 runs (10 products × 3), 0 parse failures | Markdown fences around the JSON |
| 2e | Claim checker: every claim must exist in user input | Invented "waterproof" or "50% off" gets flagged | This is the legal-risk guard |
| 2f | Language support (English, Hindi, Gujarati) | Output is in the right language, with no mixed scripts | Weak Gujarati quality in free models |

---

## Sub-phase details

### 2a

#### Build
LLM adapter with one provider (Gemini free)

#### Pass check
Returns text for a test prompt

#### Known issues
Rate limits

### 2b

#### Build
Retry with backoff, plus a second provider (Groq) as fallback

#### Pass check
Fallback triggers when the first is blocked on purpose

#### Known issues
Different output style per model

### 2c

#### Build
Prompt that produces the brief: hook, 3 benefits, tone, CTA, scene list

#### Pass check
Readable brief for all 10 products

#### Known issues
Generic wording

### 2d

#### Build
Force strict JSON and validate with pydantic

#### Pass check
30 runs (10 products × 3), 0 parse failures

#### Known issues
Markdown fences around the JSON

### 2e

#### Build
Claim checker: every claim must exist in user input

#### Pass check
Invented "waterproof" or "50% off" gets flagged

#### Known issues
This is the legal-risk guard

### 2f

#### Build
Language support (English, Hindi, Gujarati)

#### Pass check
Output is in the right language, with no mixed scripts

#### Known issues
Weak Gujarati quality in free models
