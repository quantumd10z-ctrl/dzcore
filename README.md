# Descargas de archivos grandes (alojadas en MEGA)

Este repositorio enlaza archivos grandes alojados en MEGA en lugar de incluirlos en Git (para no inflar el historial). Aquí también explicamos cómo generar las sumas SHA-256 para que cualquiera pueda verificar la integridad de una descarga.

Contenido del repositorio
- links.txt — lista de enlaces MEGA (uno por línea).
- scripts/download_all.sh — script para descargar los enlaces con MEGAcmd y calcular SHA-256.
- CHECKSUMS.sha256 — archivo donde se guardan las sumas SHA-256 oficiales (formato: "<sha256>  <nombre_del_archivo>").
- .gitignore — evita subir la carpeta downloads/ y binarios pesados.

Privacidad
- Si los archivos no son públicos, guarda este repositorio como privado en GitHub.
- Las URLs de MEGA y sus claves se muestran en links.txt: trata ese archivo como sensible si no quieres que cualquiera descargue los ficheros.

Cómo generar las sumas SHA-256 (para el que sube los archivos)
1. Descarga el archivo a tu máquina local (o calcula la suma en el servidor donde esté el archivo).
2. Usa uno de estos comandos según tu sistema:
   - Linux:
     sha256sum nombre_del_archivo.ext
   - macOS:
     shasum -a 256 nombre_del_archivo.ext
   - Windows PowerShell:
     Get-FileHash -Algorithm SHA256 .\nombre_del_archivo.ext
3. Copia la salida (la suma hex) y añade una línea en CHECKSUMS.sha256 con el formato:
   <sha256>  <nombre_del_archivo.ext>
   Ejemplo:
   e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  archivo.zip
4. Opcional pero recomendado: firma CHECKSUMS.sha256 con tu clave GPG para que los usuarios confirmen la autenticidad:
   gpg --armor --output CHECKSUMS.sha256.asc --detach-sign CHECKSUMS.sha256

Cómo verificar al descargar (para el usuario que quiere certificación)
1. Descarga el/los archivo(s) (recomendado usar megadl o la web de MEGA).
2. Calcula la suma localmente con los mismos comandos que arriba.
3. Comprueba que la suma coincide con la entrada en CHECKSUMS.sha256:
   - Linux/macOS:
     sha256sum -c CHECKSUMS.sha256
     (esto requiere que CHECKSUMS.sha256 contenga exactamente el nombre de archivo descargado)
   - O compara manualmente:
     sha256sum archivo descargado | awk '{print $1}'
     y compara con la entrada en CHECKSUMS.sha256
4. Si CHECKSUMS.sha256 está firmada (CHECKSUMS.sha256.asc), verifica la firma:
   gpg --verify CHECKSUMS.sha256.asc CHECKSUMS.sha256

Consejos prácticos
- No subas archivos grandes al repo; usa Git LFS solo si quieres integrarlo con Git y entiendes sus cuotas.
- Mantén links.txt y CHECKSUMS.sha256 en el repo (privado si es necesario) y no incluyas los binarios.
- Para reproducibilidad, indica la fecha y el tamaño del archivo en README junto con la suma.
- Si quieres que el proceso sea auditado, añade la firma GPG del autor de los checksums.

Ejemplo rápido de flujo del uploader
1. Subir archivo a MEGA (web o MEGAcmd).
2. Obtener nombre de archivo y calcular SHA-256 localmente:
   sha256sum archivo.zip
3. Añadir línea a CHECKSUMS.sha256 y firmarla:
   git add CHECKSUMS.sha256
   git commit -m "Añadir checksum para archivo.zip"
   gpg --armor --detach-sign CHECKSUMS.sha256
   git add CHECKSUMS.sha256.asc
   git commit -m "Añadir firma GPG de CHECKSUMS"
   git push origin main
