# Login / Registration System — Simplified Design Document

A minimal authentication system covering registration, login, profile management (Full Name, Date of Birth), and a "Forgot Password" flow.

## System Architecture

```mermaid
graph TB
    subgraph FE["Frontend"]
        Pages[Register / Login / Profile / Reset Pages]
    end

    subgraph App["Backend"]
        Auth[Auth Module<br/>register / login / logout]
        User[User Module<br/>profile + password reset]
    end

    DB[(Users Table)]

    Pages --> Auth
    Pages --> User
    Auth --> DB
    User --> DB
```

## Module Breakdown

```mermaid
graph LR
    subgraph M1["Auth Module"]
        A1[Register: validate, hash password, store]
        A2[Login: verify credentials, issue session]
        A3[Logout: clear session]
    end

    subgraph M2["User Module"]
        U1[View / edit profile<br/>Full Name + DOB]
        U2[Forgot password: generate token, send email]
        U3[Reset password: validate token, set new password]
    end
```

## Call Graph
 
```mermaid
graph TD
    main((main))
 
    subgraph AuthModule["Auth Module"]
        register((register))
        login((login))
        logout((logout))
    end
 
    subgraph UserModule["User Module"]
        profile((manage_profile))
        forgot((forgot_password))
        reset((reset_password))
    end
 
    subgraph Helpers["Shared Helpers"]
        validate((validate_input))
        hash((hash_password))
        token((gen_reset_token))
        email((send_email))
        db[(db_access)]
    end
 
    main --> register
    main --> login
    main --> logout
    main --> profile
    main --> forgot
    main --> reset
 
    register --> validate
    register --> hash
    register --> db
 
    login --> hash
    login --> db
 
    logout --> db
 
    profile --> validate
    profile --> db
 
    forgot --> token
    forgot --> email
    forgot --> db
 
    reset --> token
    reset --> hash
    reset --> db
```
 
## Function Responsibilities
 
| Layer | Function | Responsibility |
|-------|----------|----------------|
| Entry | `main` | Application entry point, routes to all feature functions |
| Auth | `register` | Handle registration (Full Name, Date of Birth, credentials) |
| Auth | `login` | Verify credentials and issue a session |
| Auth | `logout` | Clear the active session |
| User | `manage_profile` | View and edit profile (Full Name + DOB) |
| User | `forgot_password` | Generate a reset token and send the reset email |
| User | `reset_password` | Validate token and set a new password |
| Helper | `validate_input` | Validate and sanitise user input |
| Helper | `hash_password` | Hash a plaintext password (e.g. bcrypt) |
| Helper | `gen_reset_token` | Generate a time-limited password-reset token |
| Helper | `send_email` | Send transactional email (reset link) |
| Helper | `db_access` | Unified data-access layer (insert / query / update) |

## Registration & Login Flow

```mermaid
sequenceDiagram
    participant U as User
    participant API as Backend
    participant DB as Database

    Note over U,DB: Registration
    U->>API: Full Name / DOB / email / password
    API->>API: Validate + hash password
    API->>DB: Insert user record
    API-->>U: Success, go to login

    Note over U,DB: Login
    U->>API: email + password
    API->>DB: Query user
    API->>API: Compare password hash
    alt Valid
        API-->>U: Login success (session)
    else Invalid
        API-->>U: Credential error
    end
```

## Forgot Password Flow

```mermaid
sequenceDiagram
    participant U as User
    participant API as Backend
    participant DB as Database
    participant Mail as Email

    U->>API: Enter registered email
    API->>API: Generate time-limited reset token
    API->>DB: Save token + expiry on user row
    API->>Mail: Send reset link
    Mail-->>U: Email received
    U->>API: Open link + set new password
    API->>DB: Validate token + expiry
    alt Valid
        API->>DB: Update password, clear token
        API-->>U: Reset success
    else Expired / invalid
        API-->>U: Reject, prompt to re-request
    end
```

## Data Model

```mermaid
erDiagram
    USERS {
        int id PK
        string email UK
        string password_hash
        string full_name
        date date_of_birth
        string reset_token
        datetime reset_expires
    }
```

## Design Principles

- **Maintainability** — Only two backend modules (Auth, User) with clear responsibilities; no redundant controller/service split.
- **Scalability** — Modules are independent, so features like two-factor auth or a separate reset-token table can be added later without restructuring.
- **Readability** — A single table and a small set of flows mean newcomers can grasp the whole system at a glance.


