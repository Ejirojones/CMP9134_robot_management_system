# CBSE Interface Specification – Mission Logger Component

## Component Overview

The Mission Logger is a standalone backend component responsible for creating and retrieving the audit trail of robot commands. It supports accountability, safety investigation, and system transparency by recording who issued a command, what action was requested, when it occurred, and whether the command succeeded or failed.

This component is designed according to Component-Based Software Engineering (CBSE) principles, where the component is defined by the services it provides and the external services it requires. 

## Provides Interface

The Mission Logger provides the following services to the rest of the system:

- `logCommand(username, action, x, y, outcome)`  
  Records a robot command in the audit trail.

- `getLogs()`  
  Returns stored mission log entries for review.

- `exportLogs()`  
  Exports the mission logs for reporting or audit purposes.

## Requires Interface

The Mission Logger requires the following external services:

- **Database Connection**  
  Needed to persist mission log records in local storage.

- **System Clock / Timestamp Service**  
  Needed to generate the timestamp for each log entry.

- **Validated Command Data from Backend**  
  Needed so that only processed and authorised command results are stored.

## Responsibility Summary

The Mission Logger does not decide whether a command is allowed and does not communicate directly with the Virtual Robot API. Its sole responsibility is to persist and retrieve audit information once command processing has already occurred. This separation of concerns improves maintainability and supports the assignment requirement for a persistent mission log. 

## Interface Sketch

```mermaid
flowchart LR

Backend[Backend API / Robot Controller]

subgraph Logger[Mission Logger Component]
    Provides((Provides Interface))
    Requires((Requires Interface))
end

DB[(Database Connection)]
Clock[System Clock / Timestamp Service]

Backend -->|logCommand(), getLogs(), exportLogs()| Provides
Requires --> DB
Requires --> Clock 