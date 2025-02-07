# -*- coding: utf-8 -*-
"""PRUEBA PROYECTO V.

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1K_pn7qL8d35boMoiloSUCKxdzJnBrVaq
"""

df = pd.read_excel('PROYECTOS MODALIDAD II PROABIM 2023.xlsx', sheet_name=None)

#### PAQUETES #######
import pandas as pd
from io import BytesIO
import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

                                                                                ###### DATOS ######
file_path = 'PROYECTOS MODALIDAD II PROABIM 2023.xlsx'

df = pd.read_excel(next(iter(uploaded)),sheet_name=None)

xls = pd.ExcelFile(file_path)

xls = pd.ExcelFile(file_path)

df = pd.read_excel('PROYECTOS MODALIDAD II PROABIM 2023.xlsx', sheet_name=None)
# Cargar las hojas de datos
transferencias_df = pd.read_excel(xls, sheet_name='TRANSFERENCIAS')
proyectos_eje1_df = pd.read_excel(xls, sheet_name='EJECUCION DE PROYECTOS EJE 1')
proyectos_eje2_df = pd.read_excel(xls, sheet_name='EJECUCIÓN DE PROYECTOS EJE 2')
gastos_operativos_df = pd.read_excel(xls, sheet_name='GASTOS OPERATIVOS')

# Mostrar las primeras filas de cada DataFrame
transferencias_df.head(), proyectos_eje1_df.head(), proyectos_eje2_df.head(), gastos_operativos_df.head()

transferencias_df = pd.read_excel(xls, sheet_name='TRANSFERENCIAS')

transferencias_df.columns = transferencias_df.columns.str.strip()

transferencias_df_clean = transferencias_df[['Municipio', 'Fecha Transferencia', 'Monto', 'Proyecto/Programa', 'Estado']]

# Verificar los primeros datos
transferencias_df_clean.head()

# Asegurarnos de que los datos de 'Fecha Transferencia' sean de tipo fecha
transferencias_df_clean['Fecha Transferencia'] = pd.to_datetime(transferencias_df_clean['Fecha Transferencia'], errors='coerce')

# Verificar las primeras filas después de convertir la fecha
transferencias_df_clean.head()

# Verificar si hay valores nulos en la columna 'Fecha Transferencia'
transferencias_df_clean['Fecha Transferencia'].isnull().sum()

# Verificar el tipo de datos de la columna 'Fecha Transferencia'
transferencias_df_clean['Fecha Transferencia'].dtype

proyectos_eje2_df = pd.read_excel(xls, sheet_name='EJECUCIÓN DE PROYECTOS EJE 2')

data_eje2 = {
    'Municipio': ['Atlatahucan', 'Ayala', 'Cuautla', 'Huitzilac', 'Miacatlán', 'Tepalcingo', 'Tetecala', 'Tetela del Volcán', 'Tlalnepantla', 'Tlayacapan', 'Totolapan', 'Xochitepec'],
    'Monto Eje 2': [960000, 96000, 96000, 96000, 96000, 96000,96000,96000,96000,96000,96000,96000],
    'Monto Ejercido': [55000, 75000, 80000, 60000, 80000, 75000, 60000, 75000, 65000, 70000, 65000, 80000],
    'Personas Beneficiadas': [40, 50, 60, 60, 50, 70, 50, 60, 60, 50, 70, 60],
    'Inversión per Cápita': [1375.00, 1500.00, 1333.33, 1000.00, 1600.00, 1071.43, 1200.00, 1250.00, 1083.33, 1400.00, 928.57, 1333.33 ],
    'Porcentaje Ejercido Eje 2': [57.0, 78.0, 83.0, 63.0, 83.0, 78.0, 63.0, 78.0, 68.0, 73.0, 68.0, 83.0]
}
proyectos_eje2_df = pd.DataFrame(data_eje2)

# Datos para los gráficos de "Avance en la ejecución de recursos asignados"
avance_eje1 = {
    'Municipio': ['Atlatahucan', 'Ayala', 'Cuautla', 'Huitzilac', 'Miacatlán', 'Tepalcingo', 'Tetecala', 'Tetela del Volcán', 'Tlalnepantla', 'Tlayacapan', 'Totolapan', 'Xochitepec'],
    'Avance Eje I (%)': [60, 55, 85, 40, 80, 70, 90, 75, 85, 60, 65, 80]
}
avance_eje1_df = pd.DataFrame(avance_eje1)

avance_eje2 = {
    'Municipio': ['Atlatahucan', 'Ayala', 'Cuautla', 'Huitzilac', 'Miacatlán', 'Tepalcingo', 'Tetecala', 'Tetela del Volcán', 'Tlalnepantla', 'Tlayacapan', 'Totolapan', 'Xochitepec'],
    'Avance Eje II (%)': [65, 70, 90, 50, 85, 75, 95, 80, 90, 65, 70, 85]
}
avance_eje2_df = pd.DataFrame(avance_eje2)


# Inicializar la aplicación Dash
app = dash.Dash(__name__)

# Crear el DataFrame (reemplazar con tus datos reales)
transferencias_df_clean = pd.DataFrame({
    'Municipio': ['Atlatahucan', 'Ayala', 'Cuautla', 'Huitzilac', 'Miacatlán', 'Tepalcingo', 'Tetecala', 'Tetela del Volcán', 'Tlalnepantla', 'Tlayacapan', 'Totolapan', 'Xochitepec'],
    'Monto': [200000, 200000, 200000, 200000, 200000, 200000, 200000, 200000, 200000, 200000, 200000, 200000],
    'Estado': ['Transferido', 'Transferido ', 'Transferido', 'Transferido', 'Transferido','Transferido','Transferido','Transferido','Transferido','Transferido','Transferido','Transferido']
})


# Crear una columna para saber si el estado es 'Terminado'
transferencias_df_clean['Terminado'] = transferencias_df_clean['Estado'].apply(lambda x: 'TRANSFERIDO' if x == 'Terminado' else '')

# Crear el DataFrame 'proyectos_eje1_df' (ejemplo basado en los datos que compartiste)
proyectos_eje1_df = pd.DataFrame({
    'ID Proyecto': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'Municipio': ['Atlatahucan', 'Ayala', 'Cuautla', 'Huitzilac', 'Miacatlán', 'Tepalcingo', 'Tetecala', 'Tetela del Volcán', 'Tlalnepantla', 'Tlayacapan', 'Totolapan', 'Xochitepec'],
    'Fecha Reporte': ['2023-10-30'] * 12,
    'Avance(%)': [0.86, 0.70, 0.65, 0.75, 0.70, 0.68, 0.69, 0.75, 0.70, 0.70, 0.80, 0.85],
    'Monto Eje 1': [100000] * 12,
    'Monto Ejercido': [86000, 70000, 65000, 75000, 70000, 68000, 69000, 75000, 70000, 80000, 85000, 75000],
    'Comentarios': ['1. Apoyar en la...'] * 12,
    'Personas Beneficiados(Reportados al mes de octubre)': [70, 65, 70, 79, 50, 65, 85, 65, 70, 83, 74, 115],
    'Inversión per Cápita': [1228.57, 1076.92, 928.57, 949.37, 1400.00, 1046.15, 811.76, 1153.85, 1000.00, 963.86, 1148.65, 652.17]
})

# Calcular el porcentaje de recursos ejercidos
proyectos_eje1_df['Porcentaje Ejercido'] = (proyectos_eje1_df['Monto Ejercido'] / proyectos_eje1_df['Monto Eje 1']) * 100



# Leer la hoja 'GASTOS OPERATIVOS'
gastos_operativos_df = pd.read_excel(xls, sheet_name='GASTOS OPERATIVOS')

# Supongamos que los datos tienen columnas similares a las siguientes: 'Municipio', 'Monto de Gastos Operativos', 'Monto ejercido'
# Asegúrate de ajustar los nombres de las columnas según lo que realmente contiene tu hoja
gastos_operativos_df = gastos_operativos_df[['Municipio', 'Monto de Gastos Operativos (Proporción establecida en las ROP 7%)', 'Monto Ejercido']]


meses_df = pd.read_excel(xls, sheet_name='MESES')

gasto_programado = meses_df.iloc[0, 1:].values  # Gasto programado (sin incluir la columna 'MES')
mujeres_beneficiadas = meses_df.iloc[1, 1:].values  # Mujeres beneficiadas (sin incluir la columna 'MES')

# Definir los meses
meses = meses_df.columns[1:]  # Los meses son las columnas a partir de la segunda

meses_df = pd.read_excel(xls, sheet_name='MESES')

gasto_programado = meses_df.iloc[0, :].values  # Gasto programado (todas las columnas excepto 'MES')
mujeres_beneficiadas = meses_df.iloc[1, :].values  # Mujeres beneficiadas (todas las columnas excepto 'MES')

# Extraer los meses (que son los índices)
meses = meses_df.index.values

meses_df.set_index(meses_df.columns[0], inplace=True)

# Extraer los valores para "Gasto programado" y "Mujeres beneficiadas"
gasto_programado = meses_df.loc['Gasto programado'].values  # Extraemos los valores de 'Gasto programado'
mujeres_beneficiadas = meses_df.loc['Total de mujeres beneficiadas por los procesos de capacitación y formación para concluir sus estudios alcanzadas.'].values  # Extraemos los valores de 'Mujeres beneficiadas'

# Extraer los nombres de los meses, que están en las columnas (Mayo, Junio, Julio, etc.)
meses = meses_df.columns.values  # Los meses corresponden a las columnas del DataFrame

# Extraer los valores para "Gasto programado" y "Mujeres beneficiadas"
gasto_programado = meses_df.loc['Gasto programado'].values  # Extraemos los valores de 'Gasto programado'
mujeres_beneficiadas = meses_df.loc['Total de mujeres beneficiadas por los procesos de capacitación y formación para concluir sus estudios alcanzadas.'].values  # Extraemos los valores de 'Mujeres beneficiadas'

# Extraer los nombres de los meses, que están en las columnas (Mayo, Junio, Julio, etc.)
meses = meses_df.columns.values  # Los meses corresponden a las columnas del DataFrame

# Crear el DataFrame 'proyectos_eje1_df' (ejemplo basado en los datos que compartiste)
proyectos_eje1_df = pd.DataFrame({
    'ID Proyecto': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'Municipio': ['Atlatahucan', 'Ayala', 'Cuautla', 'Huitzilac', 'Miacatlán', 'Tepalcingo', 'Tetecala', 'Tetela del Volcán', 'Tlalnepantla', 'Tlayacapan', 'Totolapan', 'Xochitepec'],
    'Fecha Reporte': ['2023-10-30'] * 12,
    'Avance(%)': [0.86, 0.70, 0.65, 0.75, 0.70, 0.68, 0.69, 0.75, 0.70, 0.70, 0.80, 0.85],
    'Monto Eje 1': [100000] * 12,
    'Monto Ejercido': [86000, 70000, 65000, 75000, 70000, 68000, 69000, 75000, 70000, 80000, 85000, 75000],
    'Comentarios': ['1. Apoyar en la...'] * 12,
    'Personas Beneficiados(Reportados al mes de octubre)': [70, 65, 70, 79, 50, 65, 85, 65, 70, 83, 74, 115],
    'Inversión per Cápita': [1228.57, 1076.92, 928.57, 949.37, 1400.00, 1046.15, 811.76, 1153.85, 1000.00, 963.86, 1148.65, 652.17]
})

# Calcular el porcentaje de recursos ejercidos
proyectos_eje1_df['Porcentaje Ejercido'] = (proyectos_eje1_df['Monto Ejercido'] / proyectos_eje1_df['Monto Eje 1']) * 100





                                                                       #####GRÁFICOS####

fig_eje1 = px.bar(proyectos_eje1_df,
                  x='Porcentaje Ejercido',  # Porcentaje de recursos ejercidos
                  y='Municipio',  # Los municipios estarán en el eje Y
                  title="Porcentaje de Recursos Ejecutados por Municipio",  # Título del gráfico
                  labels={'Porcentaje Ejercido': 'Porcentaje de Recursos Ejecutados', 'Municipio': 'Municipio'},
                  range_x=[0, 100],  # El rango del eje X va de 0% a 100%
                  hover_data={'Municipio': True, 'Porcentaje Ejercido': True, 'Comentarios': True})  # Mostrar los comentarios en el hover

# Colores personalizados para las barras
colores = ['#1607fa', '#5038fb', '#8a69fd', '#c59bfe', '#ffccff', '#1607fa', '#5038fb', '#8a69fd', '#c59bfe', '#ffccff', '#1607fa', '#5038fb']

# Asignar colores personalizados a las barras
fig_eje1.update_traces(marker=dict(color=colores))

# Personalización de la apariencia del gráfico
fig_eje1.update_layout(
    plot_bgcolor='rgba(0, 0, 0, 1)',  # Fondo negro
    paper_bgcolor='rgba(0, 0, 0, 1)',  # Fondo de la página también negro
    font=dict(color='white'),  # Texto blanco
    title_font=dict(size=24, family='PT Serif', color='white'),  # Título blanco con tamaño ajustado
    showlegend=False,  # Desactivamos la leyenda
    xaxis=dict(
        title='Porcentaje de Recursos Ejecutados correspondientes al Eje I (Monto $100,000.00)',
        title_font=dict(size=16, family='Arial, sans-serif', color='white'),
        tickfont=dict(size=14, family='Arial, sans-serif', color='white'),
        tickmode='array',
        tickvals=[0, 20, 40, 60, 80, 100],
        ticktext=['0%', '20%', '40%', '60%', '80%', '100%'],
        gridcolor='rgba(255, 255, 255, 0.1)'  # Líneas de la cuadrícula muy suaves
    ),
    yaxis=dict(
        title='Municipio',
        title_font=dict(size=16, family='Arial, sans-serif', color='white'),
        tickfont=dict(size=14, family='Arial, sans-serif', color='white'),
        showgrid=False  # Eliminar las líneas de la cuadrícula vertical
    ),
)

# Crear el DataFrame 'transferencias_df_clean'
transferencias_df_clean = pd.DataFrame({
    'Municipio': ['Atlatahucan', 'Ayala', 'Cuautla', 'Huitzilac', 'Miacatlán', 'Tepalcingo', 'Tetecala', 'Tetela del Volcán', 'Tlalnepantla', 'Tlayacapan', 'Totolapan', 'Xochitepec'],
    'Monto': [200000, 200000, 200000, 200000, 200000, 200000, 200000, 200000, 200000, 200000, 200000, 200000],
    'Estado': ['Terminado', 'Terminado', 'Terminado', 'Terminado', 'Terminado','Terminado','Terminado','Terminado','Terminado','Terminado','Terminado','Terminado']
})

# Crear una columna para saber si el estado es 'Terminado'
transferencias_df_clean['Terminado'] = transferencias_df_clean['Estado'].apply(lambda x: 'Terminado' if x == 'Terminado' else '')

# Crear la visualización con barras horizontales
fig = px.bar(transferencias_df_clean,
             x='Monto',  # El monto será el valor en el eje X
             y='Municipio',  # Los municipios estarán en el eje Y
             title="Municipios con recursos transferidos",  # Título de la gráfica
             color='Estado',  # Colorear las barras según el estado del proyecto
             labels={'Monto': 'Monto Transferido', 'Municipio': 'Municipio'},
             range_x=[0, transferencias_df_clean['Monto'].max() + 50000],  # Ajustar el rango del eje X
             hover_data={'Municipio': True, 'Estado': True})  # Datos para el hover

# Asignar colores personalizados a las barras (color1, color2, etc.)
fig.update_traces(marker=dict(color=['#1305fb', '#351dfc', '#5835fd', '#7b4cfe', '#9e64ff', '#1305fb', '#351dfc', '#5835fd', '#7b4cfe', '#9e64ff', '#1305fb', '#351dfc']))

# Añadir un ícono de cumplimiento (check) sobre las barras para "TRANSFERIDO"
fig.update_traces(
    text=[  # Añadir icono de check donde corresponda
        '<i class="fas fa-check" style="color:#297e1d; font-size:22px;"></i>' if estado == 'Terminado' else ''
        for estado in transferencias_df_clean['Terminado']
    ],
    textposition='inside',  # Coloca el icono dentro de la barra
    textfont=dict(family="Arial, sans-serif", size=22),  # Ajustar el tamaño del ícono
    offsetgroup=1  # Desplazamiento para que no se solapen los iconos
)

# Configuración de la animación suave
fig.update_layout(
    transition={'duration': 800, 'easing': 'cubic-in-out'},  # Suaviza la animación de transición
    xaxis=dict(range=[0, transferencias_df_clean['Monto'].max() + 50000]),
    plot_bgcolor='rgba(0, 0, 0, 1)',  # Fondo negro
    paper_bgcolor='rgba(0, 0, 0, 1)',  # Fondo de la página también negro
    font=dict(color='white'),  # Texto blanco
    title_font=dict(size=30, family='Arial, sans-serif', color='white'),  # Título blanco
    coloraxis_colorbar_tickvals=[0, 1],
    coloraxis_colorbar_ticktext=['Terminado', 'Pendiente'],
    showlegend=False  # Aquí desactivamos la leyenda
)




fig_eje1 = px.bar(proyectos_eje1_df,
                  x='Porcentaje Ejercido',  # Porcentaje de recursos ejercidos
                  y='Municipio',  # Los municipios estarán en el eje Y
                  title="Porcentaje de Recursos Ejecutados por Municipio",  # Título del gráfico
                  color='Porcentaje Ejercido',  # Colorear las barras según el porcentaje de ejecución
                  labels={'Porcentaje Ejercido': 'Porcentaje de Recursos Ejecutados', 'Municipio': 'Municipio'},
                  range_x=[0, 100],  # El rango del eje X va de 0% a 100%
                  hover_data={'Municipio': True, 'Porcentaje Ejercido': True})  # Datos para el hover

fig_eje1.update_layout(
    plot_bgcolor='rgba(0, 0, 0, 1)',  # Fondo negro
    paper_bgcolor='rgba(0, 0, 0, 1)',  # Fondo de la página también negro
    font=dict(color='white'),  # Texto blanco
    title_font=dict(size=24, family='PT Serif', color='white'),  # Título blanco con tamaño ajustado
    showlegend=False,  # Desactivamos la leyenda
    xaxis=dict(
        title='Porcentaje de Recursos Ejecutados correspondientes al Eje I (Monto $100,000.00)',
        title_font=dict(size=16, family='Arial, sans-serif', color='white'),
        tickfont=dict(size=14, family='Arial, sans-serif', color='white'),
        tickmode='array',
        tickvals=[0, 20, 40, 60, 80, 100],
        ticktext=['0%', '20%', '40%', '60%', '80%', '100%'],
        gridcolor='rgba(255, 255, 255, 0.1)'  # Líneas de la cuadrícula muy suaves
    ),
    yaxis=dict(
        title='Municipio',
        title_font=dict(size=16, family='Arial, sans-serif', color='white'),
        tickfont=dict(size=14, family='Arial, sans-serif', color='white'),
        showgrid=False  # Eliminar las líneas de la cuadrícula vertical
    ),
)


# Personalización de la apariencia del gráfico
fig_eje1.update_layout(
    plot_bgcolor='rgba(0, 0, 0, 1)',  # Fondo negro
    paper_bgcolor='rgba(0, 0, 0, 1)',  # Fondo de la página también negro
    font=dict(color='white'),  # Texto blanco
    title_font=dict(size=24, family='Arial, sans-serif', color='white'),  # Título blanco con tamaño más pequeño
    coloraxis_colorbar_tickvals=[0, 100],
    coloraxis_colorbar_ticktext=['0%', '100%'],
    showlegend=False,  # Desactivamos la leyenda
    xaxis=dict(
        title='Porcentaje de Recursos Ejecutados (Monto total del eje: $100,000.00)',
        title_font=dict(size=16, family='Arial, sans-serif', color='white'),
        tickfont=dict(size=14, family='Arial, sans-serif', color='white'),
        tickmode='array',
        tickvals=[0, 20, 40, 60, 80, 100],
        ticktext=['0%', '20%', '40%', '60%', '80%', '100%'],
        gridcolor='rgba(255, 255, 255, 0.1)'  # Líneas de la cuadrícula muy suaves
    ),
    yaxis=dict(
        title='Municipio',
        title_font=dict(size=16, family='Arial, sans-serif', color='white'),
        tickfont=dict(size=14, family='Arial, sans-serif', color='white'),
        showgrid=False  # Eliminar las líneas de la cuadrícula vertical
    ),
    coloraxis=dict(
        colorscale=[  # Definiendo la paleta de colores
            [0.0, '#1305fb'],
            [0.2, '#351dfc'],
            [0.4, '#5835fd'],
            [0.6, '#7b4cfe'],
            [0.8, '#9e64ff'],
            [1.0, '#9e64ff']
        ],
    )
)


# Crear el gráfico de barras horizontales (porcentaje de recursos ejecutados)
fig_eje1 = go.Figure()



# Configuración de la animación suave
fig.update_layout(
    transition={'duration': 800, 'easing': 'cubic-in-out'},  # Suaviza la animación de transición
    xaxis=dict(range=[0, transferencias_df_clean['Monto'].max() + 50000]),
    plot_bgcolor='rgba(0, 0, 0, 1)',  # Fondo negro
    paper_bgcolor='rgba(0, 0, 0, 1)',  # Fondo de la página también negro
    font=dict(color='white'),  # Texto blanco
    title_font=dict(size=30, family='Arial, sans-serif', color='white'),  # Título blanco
    coloraxis_colorbar_tickvals=[0, 1],
    coloraxis_colorbar_ticktext=['Terminado', 'Pendiente'],
    showlegend=False  # Aquí desactivamos la leyenda
)


# Crear el DataFrame 'transferencias_df_clean'
transferencias_df_clean = pd.DataFrame({
    'Municipio': ['Atlatahucan', 'Ayala', 'Cuautla', 'Huitzilac', 'Miacatlán', 'Tepalcingo', 'Tetecala', 'Tetela del Volcán', 'Tlalnepantla', 'Tlayacapan', 'Totolapan', 'Xochitepec'],
    'Monto': [200000] * 12,
    'Estado': ['Terminado'] * 12
})

# Crear una columna para saber si el estado es 'Terminado'
transferencias_df_clean['Terminado'] = transferencias_df_clean['Estado'].apply(lambda x: 'Terminado' if x == 'Terminado' else '')

# Crear la visualización con barras horizontales
fig_transferencias = go.Figure()

for i, municipio in enumerate(transferencias_df_clean['Municipio']):
    fig_transferencias.add_trace(go.Bar(
        x=[transferencias_df_clean[transferencias_df_clean['Municipio'] == municipio]['Monto'].values[0]],
        y=[municipio],
        orientation='h',
        marker_color=['#1305fb', '#351dfc', '#5835fd', '#7b4cfe', '#9e64ff', '#1305fb', '#351dfc', '#5835fd', '#7b4cfe', '#9e64ff', '#1305fb', '#351dfc'][i % 12],
        name=municipio
    ))

    fig_gastos_operativos = go.Figure([
    go.Bar(
        y=gastos_operativos_df['Municipio'],
        x=gastos_operativos_df['Monto Ejercido'],
        orientation='h',
        marker_color='#f5a941',  # Color de las barras
        name="Monto Ejercido"
    )
])

# Configurar el diseño del gráfico
fig_gastos_operativos.update_layout(
    title="Monto Ejercido en Gastos Operativos (Proporción establecida en las ROP del PROABIM (7%)",
    xaxis_title="Monto Ejercido",
    yaxis_title="Municipio",
    template='plotly_dark',  # Estilo oscuro
    height=500,  # Ajustar el tamaño del gráfico
)

# Crear el gráfico de líneas
fig_meses = go.Figure([
    # Línea para 'Gasto programado'
    go.Scatter(
        x=meses,  
        y=gasto_programado, 
        mode='lines+markers',  
        name="Gasto programado",
        line=dict(color='blue'),  
        marker=dict(color='blue')
    ),

    # Línea para 'Total de mujeres beneficiadas'
    go.Scatter(
        x=meses,  # Meses
        y=mujeres_beneficiadas,  
        mode='lines+markers',  
        name="Mujeres beneficiadas",
        line=dict(color='orange'),  
        marker=dict(color='orange')
    )
])

# Configurar el diseño del gráfico
fig_meses.update_layout(
    title="Evolución del Gasto Programado y Mujeres Beneficiadas (por mes)",
    xaxis_title="Mes",
    yaxis_title="Valor",
    template='plotly_dark',  
    height=500,  
)

# Crear el gráfico de líneas
fig_meses = go.Figure([
    # Línea para 'Gasto programado'
    go.Scatter(
        x=meses,  
        y=gasto_programado,  
        mode='lines+markers',  
        name="Gasto programado",
        line=dict(color='blue'),  
        marker=dict(color='blue')
    ),

    # Línea para 'Total de mujeres beneficiadas'
    go.Scatter(
        x=meses,  # Meses
        y=mujeres_beneficiadas,  
        mode='lines+markers',  
        name="Mujeres beneficiadas",
        line=dict(color='orange'),  
        marker=dict(color='orange')
    )
])

# Configurar el diseño del gráfico
fig_meses.update_layout(
    title="Evolución del Gasto Programado y Mujeres Beneficiadas (por mes)",
    xaxis_title="Mes",
    yaxis_title="Valor",
    template='plotly_dark', 
    height=500,  # Ajustar la altura del gráfico
)





                                                                       ####LAYOUT#####

app.layout = html.Div(
    className="ddk-container",
    style={
        'backgroundColor': '#121212',  # Fondo oscuro para la página
        'color': 'white',  # Texto en blanco
        'fontFamily': 'Arial, sans-serif',
        'padding': '20px',
        'borderRadius': '15px',  # Bordes redondeados
        'boxShadow': '0 4px 10px rgba(0, 0, 0, 0.3)',  # Sombra para dar un efecto flotante
        'maxWidth': '1200px',  # Limitar el ancho máximo
        'margin': '0 auto'  # Centrar el contenido
    },
    children=[
        html.H1("PLATAFORMA DE RECURSOS FEDERALES TRANSFERIDOS MODALIDAD II DEL PROABIM 2023", style={
            'color': '#f6a93c',  # Título en blanco
            'textAlign': 'center',
            'fontSize': '28px',  # Título con un tamaño de fuente más pequeño
            'fontWeight': 'bold',
            'textTransform': 'uppercase',  # Hacer el título todo en mayúsculas
            'letterSpacing': '2px'  # Espaciado de letras para un estilo futurista
        }),
        html.H2("El presente aplicativo tiene por objeto el monitoreo de recursos y proyectos del Programa para el Adelanto, Bienestar e Igualdad de las Mujeres en el estado de Morelos", style={
            'color': 'white',  # Subtítulo en blanco
            'textAlign': 'center',
            'fontSize': '24px',
            'fontWeight': 'normal',
            'marginTop': '10px',
            'letterSpacing': '1px',  # Espaciado de letras
        }),
        dcc.Graph(
            id='barras',
            figure=fig,
            style={'height': '80vh'}  # Ajustar la altura del gráfico
        ),

        # Gráficos organizados en una cuadrícula
        html.Div(
            style={'display': 'grid', 'gridTemplateColumns': '1fr 1fr', 'gap': '30px'},
            children=[

                # Gráfico de "Avance en la ejecución de recursos asignados Eje I"
                html.Div(
                    children=[

                        dcc.Graph(
                            id='grafico-avance-eje1',
                            figure=go.Figure([

                                go.Bar(
                                    y=avance_eje1_df['Municipio'],
                                    x=avance_eje1_df['Avance Eje I (%)'],
                                    orientation='h',
                                    marker_color='#3d1fde',
                                    name="Avance Eje I"
                                )
                            ]).update_layout(
                                title="Avance en la ejecución de recursos asignados Eje I",
                                xaxis_title="Avance (%)",
                                yaxis_title="Municipio",
                                template='plotly_dark',
                                height=500
                            )
                        )
                    ]
                ),

                # Gráfico de "Avance en la ejecución de recursos asignados Eje II"
                html.Div(
                    children=[

                        dcc.Graph(
                            id='grafico-avance-eje2',
                            figure=go.Figure([

                                go.Bar(
                                    y=avance_eje2_df['Municipio'],
                                    x=avance_eje2_df['Avance Eje II (%)'],
                                    orientation='h',
                                    marker_color='#643ee6',
                                    name="Avance Eje II"
                                )
                            ]).update_layout(
                                title="Avance en la ejecución de recursos asignados Eje II",
                                xaxis_title="Avance (%)",
                                yaxis_title="Municipio",
                                template='plotly_dark',
                                height=500
                            )
                        )
                    ]
                ),
            ]
        ),

        # Gráficos de "Comparación de Personas Beneficiadas e Inversión per Cápita"
        html.Div(
            style={'display': 'grid', 'gridTemplateColumns': '1fr 1fr', 'gap': '30px', 'marginTop': '50px'},
            children=[

                # Gráfico de "Comparación de Personas Beneficiadas e Inversión per Cápita Eje I"
                html.Div(
                    children=[

                        dcc.Graph(
                            id='grafico-comparativo-personas-eje1',
                            figure=go.Figure([

                                go.Bar(
                                    x=proyectos_eje1_df['Municipio'],
                                    y=proyectos_eje1_df['Personas Beneficiados(Reportados al mes de octubre)'],
                                    marker_color='#0e03fc',
                                    name='Personas Beneficiadas'
                                ),
                                go.Bar(
                                    x=proyectos_eje1_df['Municipio'],
                                    y=proyectos_eje1_df['Inversión per Cápita'],
                                    marker_color='#f9a831',
                                    name='Inversión per Cápita'
                                )
                            ]).update_layout(
                                title="Personas Beneficiadas e Inversión per Cápita Eje I",
                                xaxis_title="Municipio",
                                yaxis_title="Valores",
                                template='plotly_dark',
                                height=500,
                                barmode='group',
                                showlegend=True  # Agregar leyenda
                            )
                        )
                    ]
                ),

                # Gráfico de "Comparación de Personas Beneficiadas e Inversión per Cápita Eje II"
                html.Div(
                    children=[

                        dcc.Graph(
                            id='grafico-comparativo-personas-eje2',
                            figure=go.Figure([

                                go.Bar(
                                    x=proyectos_eje2_df['Municipio'],
                                    y=proyectos_eje2_df['Personas Beneficiadas'],
                                    marker_color='#4626d0',
                                    name='Personas Beneficiadas'
                                ),
                                go.Bar(
                                    x=proyectos_eje2_df['Municipio'],
                                    y=proyectos_eje2_df['Inversión per Cápita'],
                                    marker_color='#f5a940',
                                    name='Inversión per Cápita'
                                )
                            ]).update_layout(
                                title="Personas Beneficiadas e Inversión per Cápita Eje II",
                                xaxis_title="Municipio",
                                yaxis_title="Valores",
                                template='plotly_dark',
                                height=500,
                                barmode='group',
                                showlegend=True  # Agregar leyenda
                            )
                        )
                    ]
                ),
            ]
        ),

        # Gráfico de "Monto Ejercido en Gastos Operativos"
        html.Div(
            children=[

                dcc.Graph(
                    id='grafico-gastos-operativos',
                    figure=fig_gastos_operativos,
                    style={'height': '50vh', 'marginTop': '50px'}  # Ajustar la altura y margen superior
                )
            ]
        ),

                dcc.Graph(
            id='grafico-evolucion',
            figure=fig_meses,
            style={'height': '40vh'}  # Ajustar la altura del gráfico
        ),
                # Cuadro de Resultados: Inversión Total Per Cápita
        html.Div(
            style={
                'backgroundColor': '#333333',  
                'color': 'white',
                'padding': '20px',
                'borderRadius': '10px',  # Bordes redondeados
                'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.2)',  
                'marginTop': '30px'
            },
            children=[
                html.H4("INVERSIÓN TOTAL PER CÁPITA EN PROCESOS DE CAPACITACIÓN Y CERTIFICACIÓN DE ESTUDIOS:",
                        style={'fontSize': '18px', 'fontWeight': 'bold'}),
                html.P("$1527.69", style={'fontSize': '24px', 'fontWeight': 'bold', 'color': '#f9a831'}),
                html.P("Cálculo de la inversión total de los proyectos entre el número de mujeres beneficiadas.",
                       style={'fontSize': '14px', 'color': 'white'})
            ]
        ),


        # Pie de página 
        html.Div(
            children=[
                html.P("ELABORADO POR LIC.C.POL.EDUARDO CABRERA GUTIÉRREZ.",
                       style={'color': 'white', 'fontSize': '14px', 'textAlign': 'center'}),
                html.P("FECHA DE ACTUALIZACIÓN: Diciembre 2023",
                       style={'color': 'white', 'fontSize': '14px', 'textAlign': 'center'}),
                html.P("CABARDO.GUTZ@GMAIL.COM",
                       style={'color': 'white', 'fontSize': '14px', 'textAlign': 'center'})
            ]
        ),
    ]
)
#####EJECUCIÓN######
server = app.server

if __name__ == '__main__':
    app.run_server(debug=True)

