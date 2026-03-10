# Open-Source License Audit – Robot Management System

## Purpose

This audit reviews the main third-party libraries and tools reused in the Robot Management System in order to identify their license types and assess whether they impose any legal restrictions on the project.

License information was verified against the official repositories/project documentation of each component.

## License Audit Table

| Component Name | Purpose in the System | License Type | Permissive or Copyleft |
|---|---|---|---|
| FastAPI | Backend web framework used to build the API endpoints | MIT License | Permissive |
| Uvicorn | ASGI server used to run the FastAPI backend locally | BSD 3-Clause License | Permissive |
| Requests | Python HTTP library used for communication with the Virtual Robot API | Apache License 2.0 | Permissive |
| SQLite | Local database engine for storing mission logs and user data | Public Domain | Permissive |
| Mermaid | Diagramming tool used to create architecture and UML diagrams in Markdown | MIT License | Permissive |

## Conclusion

Based on the current project stack, the identified reused components do not impose restrictive copyleft obligations on the Robot Management System, because all listed dependencies use permissive licenses or public-domain terms. Therefore, at the present stage of development, these dependencies do not require the Ground Control Station to adopt a matching open-source copyleft license.