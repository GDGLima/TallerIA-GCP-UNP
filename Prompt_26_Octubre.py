#import os
import google.generativeai as genai
apiKey = "AIzaSyCC_8kEum2GbGLLRrrqlsvEmyy8hpUaWTM"
genai.configure(apiKey)
#genai.configure(api_key=os.environ[])

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
  "input: ¿Existe el distrito de 26 de octubre en Piura?",
  "input 2: ¿Donde queda 26 de octubre en Piura?",
  "output: Si, existe el distrito de Veintiséis de Octubre en Piura creado el 15 de enero del 2013.",
  "output 2: El distrito de Veintiséis de Octubre se encuentra ubicado en la Provincia de Piura, al oeste de la Región homónima. Abarca una superficie de 110 km², su capital es el Asentamiento Humano San Martin.",
  "output 3: ",
  "input: ",
  "input 2: ",
  "output: ",
])

print(response.text)