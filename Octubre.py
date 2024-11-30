import os
import google.generativeai as genai
api="AIzaSyCKZEuBs0mQfUjawpL-m2zCE0_batVVxnE"
genai.configure(api_key=api)

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

response = model.generate_content([
  "input: ¿existe el distrito 26 de octubre?",
  "output: El distrito de Veintiséis de Octubre se encuentra ubicado en la Provincia de Piura, al oeste de la Región homónima. Abarca una superficie de 110 km². Su capital es el Asentamiento Humano San Martín. El distrito, está conformado por 41 asentamientos humanos y 5 urbanizaciones.",
  "input: ¿26 de octubre es un distrito de piura?",
  "output: El distrito 26 de Octubre es uno de los diez distritos que conforman la provincia de Piura, ubicada\nen el departamento de Piura, bajo la administración del Gobiemo Regional de Piura, en el norte\ndel Perú. Su capital es el AA. HH. San Martín, geográficamente abarca una superficie de 110 Km*\ny está situado en una altitud promedio de 30 msnm.",
  "input: ¿donde esta ubicado el distrito 26 de octubre?",
  "output: El distrito de Veintiséis de Octubre se encuentra en la provincia de Piura, en el departamento de Piura, en el norte del Perú. Se ubica al oeste de la región de Piura y abarca una superficie de 110 km². El distrito de Veintiséis de Octubre está conformado por 41 asentamientos humanos y 5 urbanizaciones. Su capital es el Asentamiento Humano San Martín. El distrito está atravesado por cuatro avenidas principales: Avenida Sánchez Cerro, Avenida Prolongación Grau, Avenida Don Bosco (ex Circunvalación), Avenida Juan Velasco Alvarado. También está organizado perpendicularmente por la Avenida César Vallejo, la Avenida Marcavelica, la Avenida Chulucanas y la Avenida Dren Cementado.",
  "input: 26 de octubre queda en piura",
  "output: El distrito Veintiséis de Octubre se creó mediante la Ley N*1353, denominada\n“Ley de Demarcación y Organización Territorial de la Provincia de Piura”, donde dispone\nlos límites de Piura y además, en el artículo 2 de la mencionada ley crea este distrito, sus\nasentamientos humanos y urbanizaciones correspondientes.",
  "input: ¿existe 26 de octubre?",
  "output: ",
])

print(response.text)