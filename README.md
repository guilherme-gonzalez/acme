# Parte 1 - Ingesta de datos

## 1. Stack de Tecnologias
![img](azure_datalake.png)

El stack de tecnologías propuesto para la empresa ACME sería un lakehouse en la nube, utilizando herramientas del stack de Azure con databricks.

#### **Sources**:
Las fuentes de datos se asumen que son mayormente bases de datos OLTP on premise, como Microsoft SQL Server u Oracle.

Adicionalmente tenemos en cuenta fuentes de datos como archivos de texto, o APIs.

#### **Ingestion**:
Para la ingesta de datos decidí utilizar los dataflows de ADF(Azure Data Factory) en un modelo `EL` (extract and load) para la carga de datos en el bronze layer.

En caso de que la ingesta sea un poco más complicada, se puede utilizar `Azure Functions` en una 'caja' dentro de ADF.

#### **Orquestador**: 
Para el orquestrador se utilizará ADF por su simplicidad e integración, pero si se necesita, ADF ofrece una instancia un Managed Airflow.

#### **Lakehouse**: 
Para la infraestructura de lakehouse decidí utilizar databricks y azure data lake gen2.

Esto se debe a que databricks es una plataforma de datos que maneja la integracion de spark y delta lake, 2 tecnologias que nos van a ayudar a ejecutar transacciones ACID encima de nuestro data lake.

Para storage usaremos azure data lake con tablas en formato parquet.

#### **Transformation Layers** 

Para las capas de transformación, adoptaremos la arquitectura Medallion, que consta de tres capas: Bronze, Silver y Gold.

**Bronze:** Esta capa contiene los datos en su forma más cruda, directamente extraídos de las fuentes. Aunque no es obligatorio, recomendaremos almacenar los datos en formato Parquet para facilitar su manejo y consulta en etapas posteriores.

Silver: En esta capa, los datos son validados y transformados para su uso general. Todos los datos en la capa Silver se almacenarán en formato Parquet, garantizando una estructura de datos consistente y eficiente.

Gold: La capa Gold está reservada para datos procesados y/o agregados, diseñados específicamente para análisis y reportes. Estos datos están optimizados para consultas rápidas y presentan la información en formatos fácilmente consumibles para los usuarios finales.

Gold: son datos procesados y/o aggregados, que son utilizados para reportes o analisis.

#### **versioning & CI/CD**:
Pretendemos utilizar buenas practicas del desarrollo de software, e implementar versionado de neustros ETLs, y transformaciones 

Entendido. Aquí tienes el documento redactado desde tu perspectiva como si estuvieras haciendo una recomendación a un cliente:


## Planificación y Estrategia de Implementación

#### Requerimientos Previos

Como requerimientos previos tendriamos temas de conectividad y permisos.

Para establecer la infraestructura en Azure necesitaremos permisos a la misma.

También necesitaremos hacer pruebas de conexión con las fuentes de datos que queremos migrar.

Y por ultimo antes de empezar el proceso de desarrollo, tendríamos que hacer el setup de azure y databricks.

#### Etapas de Implementación

#### **Diseño del Pipeline**
- **Definir el Proceso**: Diseñaremos el flujo de datos desde las fuentes hasta el Data Lake, detallando cómo extraer, cargar y transformar los datos.
- **Configurar Dataflows**: Crearemos los dataflows en ADF para cargar datos en la capa Bronze, y utilizaremos Azure Functions si se requiere procesamiento adicional.

#### **Desarrollo**
- **Implementar ETL**: Desarrollaremos y probaremos los procesos de Extract, Load y Transform en ADF y Databricks, asegurando que los datos se muevan y procesen correctamente.
- **Configurar ADF**: Aseguraremos que ADF gestione las tareas y dependencias de manera efectiva.

#### **Pruebas**
- **Pruebas Unitarias**: Realizaremos pruebas unitarias para cada componente del pipeline.
- **Pruebas de Integración y Rendimiento**: Evaluaremos la integración de todos los componentes y el rendimiento del pipeline con datos reales o simulados.

#### **Despliegue**
- **Implementar en Producción**: Desplegaremos el pipeline siguiendo prácticas de CI/CD para asegurar un proceso de despliegue suave.
- **Monitoreo**: Monitorearemos el pipeline después del despliegue para identificar y resolver cualquier problema rápidamente.

### Estrategia de Monitoreo
- **Monitoreo con ADF**: Utilizaremos las herramientas de monitoreo integradas de ADF para rastrear la ejecución de los dataflows y gestionar errores.
- **Alertas y Notificaciones**: Configuraremos alertas para recibir notificaciones sobre fallos o problemas en el pipeline.
- **Dashboards de Monitoreo**: Implementaremos dashboards personalizados en Azure Monitor o Power BI para obtener una visión general del estado del pipeline.

### Identificación de Puntos de Fallo
- **Posibles Fallos**:
  - **Conexiones de Datos**: Problemas de conectividad con las fuentes de datos.
  - **Transformaciones**: Errores en la lógica de transformación o problemas con los datos.
  - **Configuración de ADF**: Fallos en los dataflows o configuraciones incorrectas.
  - **Rendimiento**: Problemas de rendimiento durante la ingesta o transformación de datos.

- **Protocolo de Resolución de Incidentes**:
La gestión de incidentes se manejará via un sistema de ticketing ITSM como `Jira service management`.