Class Diagram for a Clinic (W5-A3) project

# Patient 
A person who visits the clinic. Can log in or register, and is the base class for both registered and walk-in patients.

# ClinicSystem
The central system that manages the clinic's operations. It checks slot availability, confirms appointments, and processes payments.

# Appointment 
A booking made by a patient for a specific slot. Tracks its status, calculates the booking fee, and can be confirmed.

# Payment
Represents a financial transaction tied to an appointment, recording the amount, payment method, and current status.

```mermaid
classDiagram

%% =========================
%% Inheritance
%% =========================
Patient <|-- RegisteredPatient
Patient <|-- WalkinPatient

%% =========================
%% Associations
%% =========================
ClinicSystem --> Slot : checks availability
ClinicSystem --> Appointment : manages
ClinicSystem --> Payment : processes
ClinicSystem --> Prescription : generates

Patient --> Appointment : books
Patient --> Payment : pays

Appointment --> Slot : reserves
Appointment *-- Payment : includes
Appointment --> Prescription : generates

Prescription --> Pharmacy : verified by
Pharmacy --> Prescription : prepares medication

%% =========================
%% Class Definitions
%% =========================

class ClinicSystem {
    int systemId
    String name
    checkAvailability()
    processPayment()
    confirmAppointment()
}

class Patient {
    int patientId
    String name
    String email
    String phone
    login()
    register()
}

class RegisteredPatient {
    Date registrationDate
}

class WalkinPatient {
    String visitReason
}

class Pharmacy {
    int pharmacyId
    String name
    verifyPrescription()
    prepareMedication()
}

class Prescription {
    int prescriptionId
    Date writtenAt
    String notes
    write()
}

class Slot {
    int slotId
    Date date
    Time startTime
    Time endTime
    boolean isAvailable()
}

class Appointment {
    int appointmentId
    Date appointmentDate
    String status
    calculateBookingFee()
    confirm()
}

class Payment {
    int paymentId
    double amount
    String paymentMethod
    String paymentStatus
    process()
}
```