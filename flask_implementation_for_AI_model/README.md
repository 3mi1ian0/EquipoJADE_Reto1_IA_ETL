# Implementacion de una interfaz basada en flask

##Esta API de Flask sirve como interfaz web para realizar predicciones de ventas utilizando un modelo XGBoost. Las características y componentes clave incluyen:

- **Selección desplegable**: Los usuarios pueden seleccionar varios parámetros como día, mes, número de tienda y más a través de menús desplegables.

- **Validación de entradas**: La aplicación comprueba si faltan entradas y se asegura de que los datos están dentro de los rangos esperados en el backend (no se muestra en HTML).

- **Visualización de predicciones**: Tras enviar el formulario, se muestra al usuario el valor de ventas previsto. Los errores se tratan con mensajes informativos.

- **Estilo Bootstrap**: Bootstrap se utiliza para el estilo, proporcionando una interfaz sensible y visualmente agradable.

- **Escalabilidad**: La estructura de la plantilla permite una fácil expansión con características u opciones adicionales en el futuro.

- **Consideraciones de seguridad**: Aunque no se detalla en la plantilla, los datos de entrada deben ser validados y desinfectados en el lado del servidor para evitar vulnerabilidades de seguridad.

##Plantilla HTML (index.html):

Esta plantilla HTML es la interfaz de usuario para la API de Flask. Los elementos clave y funcionalidades incluyen:

- **Menús desplegables**: Se proporcionan menús desplegables para seleccionar varios parámetros de entrada como día, mes, tipo, etc.

- **Envío de formularios**: Los usuarios pueden enviar sus selecciones a la API de Flask haciendo clic en el botón "Predecir ventas".

- **Visualización de las ventas previstas**: El valor de las ventas previstas se muestra al usuario después de enviar el formulario.

- **Gestión de errores**: Se muestran mensajes de error claros si faltan entradas.

- **Estilo responsivo**: Bootstrap se utiliza para el estilo, asegurando que la interfaz se adapta a diferentes tamaños de pantalla.

- **Diseño fácil de usar**: Las entradas están etiquetadas y organizadas de una manera fácil de usar.

- **Potencial de expansión**: La estructura de la plantilla está diseñada para dar cabida a futuras adiciones o cambios en las características de la aplicación.
