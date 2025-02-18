![imagen](https://github.com/user-attachments/assets/88558928-ec95-4dbb-b095-e0783d06a65d)**Modelos**

ContractingCompany:

![imagen](https://github.com/user-attachments/assets/0b7b833d-55a6-45c3-bfab-6ab477ff8193)

- Este modelo permite gestionar empresas contratadoras, almacenando información básica como su nombre, dirección y contacto.
Además, permite asociar múltiples proyectos a una empresa contratadora, lo que facilita la gestión de proyectos en Odoo.

Project:

![imagen](https://github.com/user-attachments/assets/1395fa4f-70c3-4142-a3de-8c729124eb25)

- Este modelo permite gestionar proyectos en Odoo, añadiendo campos para asociar una empresa contratadora y un jefe de proyecto. Además, implementa un control de permisos para que solo los usuarios con ciertos privilegios (pertenecientes a grupos específicos) puedan crear o modificar proyectos. Esto asegura que solo personas autorizadas puedan gestionar proyectos dentro del sistema.

ProjectProject:

![imagen](https://github.com/user-attachments/assets/9504bcb2-39ab-47df-9769-28b505d85b93)

- Este módulo está diseñado para gestionar la relación entre proyectos y empresas contratadoras en Odoo. Su objetivo principal es permitir la asociación de proyectos con las empresas que los contratan, facilitando la gestión de esta relación en el sistema.

Task:

![imagen](https://github.com/user-attachments/assets/6df014f7-6614-401b-ab78-204db69bd4ee)

- El módulo amplía el modelo de tareas en Odoo (project.task) para permitir la creación y gestión de subtareas dentro de cada tarea principal. Mediante el campo subtask_ids, se puede vincular una lista de subtareas a una tarea, lo que facilita la organización y descomposición de tareas complejas en tareas más pequeñas y gestionables.

Subtask:

![imagen](https://github.com/user-attachments/assets/69c62d1f-228f-4708-890c-8495e9a1f55b)

- Este módulo crea un nuevo modelo project.subtask, que representa las subtareas dentro de una tarea de un proyecto. Cada subtarea tiene un nombre, una descripción y está asociada a una tarea principal específica mediante el campo task_id.

**Vistas**

contracting_company_view:

![imagen](https://github.com/user-attachments/assets/179a4e98-cf09-48fe-aaba-8f39923a9c78)

- Este código XML define vistas para el modelo contracting.company en Odoo, lo que permite a los usuarios visualizar y gestionar empresas contratadoras dentro del sistema.

project_views:

![imagen](https://github.com/user-attachments/assets/ef1bfdde-2c2d-4f8d-abd7-8e5346d0be32)

- Este código XML define una vista heredada en Odoo para el formulario del modelo project.project. Su propósito es añadir un nuevo campo al formulario de proyectos sin modificar directamente la vista original.

task_views:

![imagen](https://github.com/user-attachments/assets/f7373cdb-86cc-493b-b389-5afa5e4005c9)

- Este código XML hereda y extiende la vista de formulario del modelo project.task en Odoo, agregando un nuevo campo que permite gestionar subtareas dentro de una tarea.

subtask_views:

![imagen](https://github.com/user-attachments/assets/9f16eb05-d443-438e-b694-31e3a1fa6d32)

- Este código XML define las vistas de árbol y formulario para el modelo project.subtask en Odoo, lo que permite la gestión de subtareas dentro del sistema de proyectos.

**Grupos de permisos (Roles):**

![imagen](https://github.com/user-attachments/assets/0bf1bae4-2aea-4fed-826f-1e0e57ac09e2)

**Grupos de usuario:**

![imagen](https://github.com/user-attachments/assets/e7848774-8899-41dd-b2df-d208a7c296e2)

**Reglas de acceso:**

![imagen](https://github.com/user-attachments/assets/64a328d4-5b4a-4e9d-aef0-3b0d10ebd3ec)

**Vistas heredadas:**

Las vistas heredadas que contiene mi proyecto, son las vistas de project_views y task_views, anteriormente mencionadas.

**Modelos heredados:**

Los modelos heredados que contiene mi proyecto, son los modelos de ProjectProject, Project y Task, anteriormente mencionados. 
