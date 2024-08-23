# Parte 1 - Ingesta de Datos

## Índice
- [Parte 1 - Ingesta de Datos](#parte-1---ingesta-de-datos)
  - [Índice](#índice)
  - [1. Stack de Tecnologías](#1-stack-de-tecnologías)
  - [2. Versionado \& CI/CD](#2-versionado--cicd)
  - [3. Planificación y Estrategia de Implementación](#3-planificación-y-estrategia-de-implementación)
    - [Requerimientos Previos](#requerimientos-previos)
    - [Etapas de Implementación](#etapas-de-implementación)
      - [Diseño del Pipeline](#diseño-del-pipeline)
      - [Desarrollo](#desarrollo)
      - [Pruebas](#pruebas)
      - [Despliegue](#despliegue)
  - [4. Estrategia de Monitoreo](#4-estrategia-de-monitoreo)
  - [5. Identificación de Puntos de Fallo](#5-identificación-de-puntos-de-fallo)
- [Parte 2 - Transformaciones de datos](#parte-2---transformaciones-de-datos)

## 1. Stack de Tecnologías
![img](azure_datalake.png)

El stack de tecnologías propuesto para la empresa ACME utiliza un enfoque de lakehouse en la nube, aprovechando las herramientas del ecosistema de Azure junto con Databricks.

**Sources**: Las fuentes de datos incluyen principalmente bases de datos OLTP on-premise como Microsoft SQL Server u Oracle, así como archivos de texto y APIs.

**Ingestion**: Utilizaremos dataflows de ADF (Azure Data Factory) en un modelo `EL` (Extract and Load) para cargar datos en la capa Bronze. Para procesos más complejos, emplearemos `Azure Functions` dentro de ADF.

**Orquestador**: ADF se encargará de la orquestación debido a su simplicidad e integración, aunque también ofrecemos la opción de Managed Airflow si se requiere.

**Lakehouse**: Optamos por Databricks y Azure Data Lake Gen2 para la infraestructura del lakehouse. Databricks integra Spark y Delta Lake, permitiendo transacciones ACID sobre el data lake. Usaremos Azure Data Lake para almacenamiento en formato Parquet.

**Capas de Transformación**: Adoptamos la arquitectura Medallion con tres capas: Bronze, Silver y Gold.

- **Bronze**: Datos crudos extraídos de las fuentes. Aunque no es obligatorio, se recomienda almacenar en formato Parquet para un manejo eficiente.
- **Silver**: Datos validados y transformados, almacenados en formato Parquet para asegurar consistencia.
- **Gold**: Datos procesados y/o agregados, optimizados para reportes y análisis.

## 2. Versionado & CI/CD
Implementaremos buenas prácticas de desarrollo de software, incluyendo versionado de ETLs y transformaciones, y utilizaremos prácticas de CI/CD para garantizar un proceso de despliegue fluido y controlado.

## 3. Planificación y Estrategia de Implementación

### Requerimientos Previos
- **Infraestructura en Azure**: Asegurarse de que Azure Data Lake Gen2 y Databricks estén configurados.
- **Conectividad**: Verificar el acceso a las fuentes de datos y permisos necesarios.
- **Configuración de Herramientas**: Confirmar la configuración de ADF y Databricks.

### Etapas de Implementación

#### Diseño del Pipeline
- **Definir el Proceso**: Planificar el flujo de datos desde las fuentes hasta el Data Lake, especificando cómo extraer, cargar y transformar los datos.
- **Configurar Dataflows**: Crear los dataflows en ADF para la capa Bronze y utilizar Azure Functions si es necesario.

#### Desarrollo
- **Implementar ETL**: Desarrollar y probar los procesos de Extract, Load y Transform en ADF y Databricks.
- **Configurar ADF**: Asegurarse de que ADF gestione las tareas y dependencias eficazmente.

#### Pruebas
- **Pruebas Unitarias**: Realizar pruebas para cada componente del pipeline.
- **Pruebas de Integración y Rendimiento**: Evaluar la integración y el rendimiento del pipeline con datos reales o simulados.

#### Despliegue
- **Implementar en Producción**: Desplegar el pipeline siguiendo prácticas de CI/CD.
- **Monitoreo**: Monitorear el pipeline para identificar y resolver problemas de manera oportuna.

## 4. Estrategia de Monitoreo
- **Monitoreo con ADF**: Utilizar las herramientas de monitoreo integradas de ADF para rastrear y gestionar la ejecución de los dataflows.
- **Alertas y Notificaciones**: Configurar alertas para notificaciones de fallos o problemas.
- **Dashboards de Monitoreo**: Implementar dashboards en Azure Monitor o Power BI para una visión general del estado del pipeline.

## 5. Identificación de Puntos de Fallo
- **Posibles Fallos**:
  - **Conexiones de Datos**: Problemas de conectividad con las fuentes de datos.
  - **Transformaciones**: Errores en la lógica de transformación.
  - **Configuración de ADF**: Fallos en dataflows o configuraciones incorrectas.
  - **Rendimiento**: Problemas durante la ingesta o transformación de datos.

- **Protocolo de Resolución de Incidentes**:
  - **Documentación y Diagnóstico**: Registrar y diagnosticar problemas detalladamente.
  - **Resolución Inicial**: Intentar resolver problemas siguiendo procedimientos estándar.
  - **Escalación**: Escalar a soporte si es necesario.

---

Espero que este formato sea más adecuado para tus necesidades. ¡Avísame si necesitas más ajustes!

# Parte 2 - Transformaciones de datos
