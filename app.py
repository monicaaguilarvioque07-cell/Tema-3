import streamlit as st
from PIL import Image, ImageDraw, ImageFont, ImageOps
import io
import os

# Configuración de la página
st.set_page_config(
    page_title="Generador de Carnés",
    layout="centered"
)

st.title("Generador de Carnés de Empleados")

# Sidebar para inputs
st.sidebar.header("Datos del Empleado")

nombre = st.sidebar.text_input("Nombre del Empleado", "JUAN PERÉZ")
cargo = st.sidebar.text_input("Cargo", "Director de Marketing")
id_empleado = st.sidebar.text_input("ID del Empleado", "EMP-7890")
color_marca = st.sidebar.color_picker("Color Corporativo", "#007bff")

# Upload de foto
st.sidebar.header("Foto de Perfil")
foto_upload = st.sidebar.file_uploader("Sube una foto", type=["jpg", "jpeg", "png"])

# Parámetros del carné
ANCHO_CARNET = 400
ALTO_CARNET = 600

if st.sidebar.button("Generar Carné", key="generate"):
    try:
        # 1. Crear lienzo base
        carnet = Image.new('RGB', (ANCHO_CARNET, ALTO_CARNET), color='white')
        draw = ImageDraw.Draw(carnet)
        
        # 2. Cargar fuentes
        try:
            font_nombre = ImageFont.truetype("arial.ttf", 35)
            font_cargo = ImageFont.truetype("arial.ttf", 20)
            font_id = ImageFont.truetype("arial.ttf", 16)
            font_footer = ImageFont.truetype("arial.ttf", 12)
        except IOError:
            font_nombre = ImageFont.load_default()
            font_cargo = ImageFont.load_default()
            font_id = ImageFont.load_default()
            font_footer = ImageFont.load_default()
        
        # 3. Dibujar Banner Superior
        draw.rectangle([0, 0, ANCHO_CARNET, 180], fill=color_marca)
        
        # 4. Procesar y Pegar Foto de Perfil
        if foto_upload is not None:
            foto_original = Image.open(foto_upload)
            foto_perfil = ImageOps.fit(foto_original, (180, 180), centering=(0.5, 0.5))
            
            # Crear máscara circular
            mask = Image.new('L', (180, 180), 0)
            mask_draw = ImageDraw.Draw(mask)
            mask_draw.ellipse((0, 0, 180, 180), fill=255)
            
            carnet.paste(foto_perfil, (110, 90), mask)
        else:
            # Placeholder si no hay foto
            draw.ellipse((110, 90, 110+180, 90+180), fill="#cccccc", outline="#666666", width=2)
            draw.text((150, 170), "SIN FOTO", fill="#333333", font=font_id)
        
        # 5. Inserción de Textos
        draw.text((ANCHO_CARNET/2, 310), nombre.upper(), font=font_nombre, fill="black", anchor="mm")
        draw.text((ANCHO_CARNET/2, 350), cargo, font=font_cargo, fill="#555555", anchor="mm")
        
        # Línea divisoria
        draw.line([120, 380, 280, 380], fill=color_marca, width=3)
        
        # ID del Empleado
        draw.text((ANCHO_CARNET/2, 410), f"ID: {id_empleado}", font=font_id, fill="black", anchor="mm")
        
        # 6. Footer del Carné
        draw.rectangle([0, ALTO_CARNET - 60, ANCHO_CARNET, ALTO_CARNET], fill="#f8f9fa")
        draw.text((ANCHO_CARNET/2, ALTO_CARNET - 30), "PROPIEDAD PRIVADA - USO INTERNO", font=font_footer, fill="#adb5bd", anchor="mm")
        
        # Mostrar preview
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.image(carnet, caption="Vista Previa del Carné", use_column_width=True)
        
        with col2:
            st.success("✅ Carné generado exitosamente")
            
            # Descargar carné
            buffer = io.BytesIO()
            carnet.save(buffer, format="PNG")
            buffer.seek(0)
            
            st.download_button(
                label="⬇️ Descargar PNG",
                data=buffer,
                file_name=f"carnet_{nombre.replace(' ', '_')}.png",
                mime="image/png"
            )
        
    except Exception as e:
        st.error(f"❌ Error al generar el carné: {str(e)}")

# Info
st.markdown("---")
st.info("💡 **Cómo usar:** Completa los datos en la barra lateral y haz clic en 'Generar Carné'")
