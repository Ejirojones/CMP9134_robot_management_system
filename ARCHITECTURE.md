# Architecture – Robot Management System

## Chosen Architectural Pattern

The Robot Management System adopts a **client–server architecture** combined with a **layered design**.

At the highest level, the system operates as a client–server application. The **Web Dashboard** acts as the client through which authorised users monitor robot telemetry and issue control commands. The **FastAPI backend** acts as the server, receiving HTTP requests, enforcing authentication and role-based access control, validating input, retrieving robot telemetry, sending movement commands to the Virtual Robot API, handling communication failures, and coordinating audit logging. This aligns directly with the assignment requirement to provide a web-based dashboard that communicates with the provided Virtual Robot API while remaining robust under connection problems. :contentReference[oaicite:0]{index=0}

Within the server side, the application also follows a layered architecture. The **presentation layer** is represented by the Web Dashboard. The **application and business logic layer** is represented by the FastAPI backend, which processes requests, applies security checks, validates coordinates, and manages robot-control workflows. The **data and integration layer** contains the local database used to persist users and mission logs, together with the external **Virtual Robot container**, which exposes the REST API used to retrieve robot status and execute robot actions. This separation of concerns improves maintainability, testability, and scalability, because each layer has a clear responsibility and can be evolved with minimal impact on the others. 

This architectural choice is appropriate for the Ground Control Station because it supports the major functional and non-functional requirements of the project. The client–server structure supports remote interaction with the robot, while the layered design supports modular development, easier debugging, and better alignment with secure software engineering practice. It also provides a sound basis for later implementation of testing, containerisation, and CI/CD, all of which are explicitly required by the assignment. 

## Tech Stack Mapping

- **Client / Presentation Layer:** Web Dashboard for monitoring status and submitting robot commands
- **Application / Business Logic Layer:** Python FastAPI backend for request handling, validation, authentication, and robot-control logic
- **Security Services:** Authentication and role-based access control implemented in the backend
- **Data Layer:** Local database for storing users and mission logs
- **External Integration Layer:** Virtual Robot Docker container exposing the robot REST API

## Architecture Diagram

```mermaid
flowchart LR

User[Commander / Viewer / Auditor]

subgraph Client[Client Layer]
    UI[Web Dashboard]
end

subgraph Server[Server Layer]
    API[FastAPI Backend]
    AUTH[Authentication and RBAC]
    LOGIC[Telemetry, Validation and Robot Control Logic]
end

subgraph Data[Data and Integration Layer]
    DB[(Local Database\nUsers + Mission Logs)]
    Robot[Virtual Robot Container]
end

User -->|Monitor telemetry / send commands| UI
UI -->|HTTP requests| API
API --> AUTH
API --> LOGIC
AUTH -->|Read user data| DB
LOGIC -->|Store audit logs| DB
LOGIC -->|REST API calls| Robot