import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviaremail(email,code,name):
    proveedor_correo = 'smtp.gmail.com: 587'
    remitente = 'codegroup787@gmail.com'
    password = 'codegroup787..'
    servidor = smtplib.SMTP(proveedor_correo)
    servidor.starttls()
    servidor.ehlo()
    servidor.login(remitente, password)
    mensaje = f"""
    <table style="border-collapse: collapse; margin: 0 auto; padding: 10px; text-align: center; position: relative;  border: 1px; width: 100%; max-width: 700px;">
        <tr>
        <td style="padding: 80px 0px 70px 0px; background-image: url(https://cdn.pixabay.com/photo/2014/11/21/03/24/mountains-540115_960_720.jpg);">
            <h2 style="font-size: 38px; color: black;">SID QUINDIO</h2>
        </td>
        </tr>
        <tr>
            <td style="padding: 20px 0px 50px 0px; background-color: rgb(224, 213, 213);">
                <div>
                    <p style=" font-size: 18px; font-weight: bold; color: black; font-family: 'Roboto', sans-serif;">Lorem ipsum dolor sit amet <span style="color: red;">{name}</span> consectetur adipisicing elit. Temporibus laudantium ipsa dolor nisi eos repellat, neque saepe sapiente nemo a, illo hic id aperiam amet quam mollitia esse perspiciatis fugit.</p>
                    <br>
                    <a href="http://localhost:4200/recover-pass/{code}" style="text-decoration: none; font-size: 23px; font-weight: 600; padding: 10px 20px; color: #FFF; background-color: rgb(44, 93, 255); border: 2px solid #0016b0; font-family: 'Chango', cursive;">Boton</a>
                </div>
            </td>
        </tr>
    </table>
    """
    msg = MIMEMultipart()
    msg.attach(MIMEText(mensaje, 'html'))
    msg['From'] = remitente
    msg['To'] = email
    msg['Subject'] = 'Prueba'
    servidor.sendmail(msg['From'] , msg['To'], msg.as_string())