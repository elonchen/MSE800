users (id, username, email, password_hash, created_at)

currencies (id, code, name, symbol)

wallets (id, user_id, currency_id, balance)

transactions (id, user_id, from_currency_id, to_currency_id, from_amount, to_amount, exchange_rate, created_at)


There are **4 tables** in total.

---

**1. `users`**
Stores account credentials and identity for each registered user. It is the root entity of the entire system — every wallet and every transaction must be tied to a real user. Without this table there is no concept of ownership or authentication.

---

**2. `currencies`**
Stores the supported currencies (e.g. USD, NZD, JPY) as a lookup reference. Rather than hardcoding currency strings like `"USD"` directly into wallets or transactions, both tables reference this one via a foreign key. This avoids data duplication and ensures consistency — if a currency's display name or symbol needs to change, you update it in one place.

---

**3. `wallets`**
Represents a user's balance in a specific currency. Because one user can hold multiple currencies, this is a many-to-many bridge between `users` and `currencies`. The `UNIQUE(user_id, currency_id)` constraint enforces that each user has at most one wallet per currency. Without this table there is nowhere to store or deduct balances when exchanges occur.

---

**4. `transactions`**
Records a permanent, immutable log of every currency exchange a user performs. It captures the source currency, target currency, both amounts, and the exchange rate at the time — providing a full audit trail. This cannot be derived from the `wallets` table alone, because wallet balances only reflect the current state, not history.

---

**Summary**

| Table | Role |
|---|---|
| `users` | Who is using the system |
| `currencies` | What currencies are supported |
| `wallets` | How much of each currency a user holds |
| `transactions` | What exchanges have taken place |

Each table captures a distinct concern, and none of them can be collapsed into another without losing either data integrity or historical information.