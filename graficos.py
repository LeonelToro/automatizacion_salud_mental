# graficos.py
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np

sns.set_palette("viridis")

def grafico_rango_edad(df, labels, output_dir, fecha_hoy):
    plt.figure(figsize=(8, 5))
    ax = sns.countplot(data=df, x='rango_edad', order=labels, palette='viridis')
    plt.xlabel('Rango de Edad')
    plt.ylabel('Cantidad de Pedidos')
    plt.title('Cantidad de pedidos por rango de edad')

    for p in ax.patches:
        height = p.get_height()
        ax.annotate(f'{int(height)}', (p.get_x() + p.get_width() / 2, height),
                    ha='center', va='bottom')
    ax.set_xticklabels([str(label) for label in labels])
    plt.tight_layout()

    filename = os.path.join(output_dir, f"grafico_rango_edad_{fecha_hoy}.png")
    plt.savefig(filename)
    plt.close()
    print(f"Gráfico guardado: {filename}")

def grafico_pie_motivos(df, output_dir, fecha_hoy):
    plt.figure(figsize=(9, 9))
    motivos_counts = df['Lo que motiva la derivación es:'].value_counts()
    colores = sns.color_palette("viridis", n_colors=len(motivos_counts))
    motivos_counts.plot.pie(autopct=lambda pct: f"{pct:.1f}%", startangle=90, counterclock=False, colors=colores)
    plt.ylabel('')
    plt.title('Distribución de motivos de derivación')
    plt.tight_layout()

    filename = os.path.join(output_dir, f"grafico_pie_motivos_{fecha_hoy}.png")
    plt.savefig(filename)
    plt.close()
    print(f"Gráfico guardado: {filename}")

def grafico_pie_tratamiento(df, output_dir, fecha_hoy):
    plt.figure(figsize=(6, 6))
    tratamiento_counts = df['¿La persona ya hizo tratamiento por salud mental alguna vez?'].value_counts()
    colores = sns.color_palette("viridis", n_colors=len(tratamiento_counts))
    tratamiento_counts.plot.pie(autopct=lambda pct: f"{pct:.1f}%", startangle=90, counterclock=False, colors=colores)
    plt.ylabel('')
    plt.title('¿La persona ya hizo tratamiento por salud mental alguna vez?')
    plt.tight_layout()

    filename = os.path.join(output_dir, f"grafico_pie_tratamiento_{fecha_hoy}.png")
    plt.savefig(filename)
    plt.close()
    print(f"Gráfico guardado: {filename}")

def grafico_lineas_consultas_por_mes(df, output_dir, fecha_hoy):
    consultas_por_mes = df.groupby('mes').size()
    colores = sns.color_palette("viridis", n_colors=1)
    color_linea = colores[0]

    plt.figure(figsize=(10, 5))
    ax = consultas_por_mes.plot(marker='o', color=color_linea)
    plt.xlabel('Mes')
    plt.ylabel('Cantidad de Consultas')
    plt.title('Cantidad de consultas por mes')
    plt.grid(True)

    # Ajustar límites del eje x para que los puntos no queden cortados
    ax.set_xlim(consultas_por_mes.index.min().start_time, consultas_por_mes.index.max().end_time)

    plt.tight_layout()

    filename = os.path.join(output_dir, f"grafico_lineas_consultas_por_mes_{fecha_hoy}.png")
    plt.savefig(filename)
    plt.close()
    print(f"Gráfico guardado: {filename}")

def grafico_barras_apiladas_semanas(df, output_dir, fecha_hoy):
    import numpy as np

    # Crear tabla dinámica: filas=mes, columnas=semana, valores=cantidad de pedidos
    pivot = df.pivot_table(index='mes', columns='semana', values='DNI', aggfunc='count', fill_value=0)

    # Ordenar columnas por semana (número de semana dentro del mes)
    # Extraigo número de semana del periodo para ordenar
    semanas_numeros = [s.week for s in pivot.columns]
    pivot = pivot.reindex(sorted(pivot.columns, key=lambda x: x.week), axis=1)

    plt.figure(figsize=(12, 6))

    max_semanas = 5
    colores = sns.color_palette("viridis", max_semanas)

    bottom = np.zeros(len(pivot))
    labels_semana = [f"Semana {i+1}" for i in range(max_semanas)]

    for i in range(max_semanas):
        # Sumamos la semana i+1 (index i)
        # No siempre la semana existe, la chequeamos:
        cols_semana = [col for col in pivot.columns if col.week == i+1]
        if not cols_semana:
            continue
        valores = pivot[cols_semana].sum(axis=1)
        plt.bar(pivot.index.astype(str), valores, bottom=bottom, color=colores[i], label=labels_semana[i])
        bottom += valores

    plt.xlabel('Mes')
    plt.ylabel('Cantidad de Pedidos')
    plt.title('Pedidos por mes y semana (colores fijos por semana)')
    plt.legend(title='Semana del mes')
    plt.tight_layout()

    filename = os.path.join(output_dir, f"grafico_barras_apiladas_semanas_{fecha_hoy}.png")
    plt.savefig(filename)
    plt.close()
    print(f"Gráfico guardado: {filename}")

def grafico_cantidad_palabras_clave(df, output_dir, fecha_hoy):
    plt.figure(figsize=(10, 6))
    order = sorted(df['cantidad_palabras_clave'].unique())
    ax = sns.countplot(data=df, x='cantidad_palabras_clave', order=order, palette='viridis')
    plt.title('Cantidad de Palabras Clave por Registro')

    for p in ax.patches:
        ax.annotate(str(int(p.get_height())),
                    (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='bottom', fontsize=10, color='black')

    plt.xlabel('Cantidad de Palabras Clave')
    plt.ylabel('Cantidad de Registros')
    plt.tight_layout()

    filename = os.path.join(output_dir, f"grafico_cantidad_palabras_clave_{fecha_hoy}.png")
    plt.savefig(filename)
    plt.close()
    print(f"Gráfico guardado: {filename}")

def grafico_top10_motivos(df, output_dir, fecha_hoy):
    grupo = df.groupby('palabras clave')['DNI'].count()
    grupo = grupo.sort_values(ascending=False)
    categorias = grupo.rename_axis('categoría').reset_index(name='cantidad')

    # Separar categorías múltiples en filas individuales
    categorias_expandidas = (
        categorias
        .assign(categoría=categorias['categoría'].str.split('/'))
        .explode('categoría')
    )

    categorias_agrupadas = (
        categorias_expandidas
        .groupby('categoría', as_index=False)['cantidad']
        .sum()
        .sort_values('cantidad', ascending=False)
    )

    categorias_agrupadas['categoría'] = categorias_agrupadas['categoría'].str.capitalize()
    top_10 = categorias_agrupadas.head(10)

    plt.figure(figsize=(10, 6))
    ax = sns.barplot(data=top_10, x='cantidad', y='categoría', palette='viridis')

    plt.title('Top 10 motivos más frecuentes', fontsize=14)
    plt.xlabel('Cantidad de casos')
    plt.ylabel('Motivo')

    for i, v in enumerate(top_10['cantidad']):
        plt.text(v + 0.5, i, str(v), va='center', fontsize=10)

    plt.tight_layout()

    filename = os.path.join(output_dir, f"grafico_top10_motivos_{fecha_hoy}.png")
    plt.savefig(filename)
    plt.close()
    print(f"Gráfico guardado: {filename}")
