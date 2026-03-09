# AI Verification Log

This document records how AI tools were used during the development of the Robot Management System and how outputs were verified.

| Task Category | AI Tool Used | Prompt Summary | Verification & Modification |
| --- | --- | --- | --- |
| Backend API Setup | ChatGPT | Requested minimal FastAPI backend for robot management system | Verified by installing dependencies, running uvicorn, and confirming the endpoint returned the expected JSON response in the browser. |
| Telemetry endpoint | ChatGPT | Asked for a structured FastAPI telemetry endpoint aligned with the robot management system requirements | Verified by running the FastAPI server locally and confirming that `/robot/status` returned telemetry data including battery level, robot position, connection status, and operational state. Adjusted the response schema to match the assignment specification. |
| Privacy policy drafting and legal review | ChatGPT | Requested an initial privacy policy for the Robot Management System | Verified the draft by checking its consistency with UK GDPR principles, the Data Protection Act 2018, and broader security and accountability requirements. Revised the wording to include the legal basis for data minimisation, purpose limitation, retention, and access control. Also ensured the content aligns with the system's actual functionality and assignment requirements. |
| Stakeholder persona analysis | ChatGPT | Asked AI to act as a warehouse robot operator reviewing telemetry and navigation features | Reviewed suggestions and incorporated relevant usability and safety requirements into Trello acceptance criteria |