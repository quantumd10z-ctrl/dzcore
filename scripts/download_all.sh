#!/usr/bin/env bash
set -euo pipefail

LINKS_FILE="links.txt"
CHECKSUM_FILE="CHECKSUMS.sha256"
OUTDIR="downloads"

if ! command -v megadl >/dev/null 2>&1; then
  echo "megadl no está instalado. Instala MEGAcmd: https://mega.nz/megacmd"
  exit 1
fi

mkdir -p "$OUTDIR"

echo "Leyendo enlaces de $LINKS_FILE..."
while IFS= read -r LINK || [ -n "$LINK" ]; do
  # Ignorar líneas vacías o comentarios
  [[ -z "
${LINK// /}" || "${LINK:0:1}" == "#" ]] && continue

  echo
  echo "Descargando: $LINK"
  megadl "$LINK" --path "$OUTDIR"

  # Detectar el archivo recién descargado (el más reciente)
  FNAME=$(ls -1t "$OUTDIR" | head -n1)
  if [[ -z "$FNAME" ]]; then
    echo "No se detectó archivo descargado en $OUTDIR"
    continue
  fi

  echo "Archivo descargado: $FNAME"

  # Calcular SHA-256
  if command -v sha256sum >/dev/null 2>&1; then
    SUM=$(sha256sum "$OUTDIR/$FNAME" | awk '{print $1}')
  else
    SUM=$(shasum -a 256 "$OUTDIR/$FNAME" | awk '{print $1}')
  fi
  echo "SHA256 calculado: $SUM"

  # Buscar checksum esperado en CHECKSUM_FILE (si existe)
  if [[ -f "$CHECKSUM_FILE" ]]; then
    EXPECTED=$(grep -E "[[:space:]]$FNAME$" "$CHECKSUM_FILE" 2>/dev/null | awk '{print $1}' || true)
    if [[ -n "$EXPECTED" ]]; then
      if [[ "$SUM" == "$EXPECTED" ]]; then
        echo "Verificación: OK"
      else
        echo "Verificación: MISMATCH (esperado: $EXPECTED)"
      fi
    else
      echo "No existe entrada en $CHECKSUM_FILE para '$FNAME'. Añádela si quieres verificar."
    fi
  else
    echo "No se encontró $CHECKSUM_FILE — crea uno con formato: <sha256>  <nombre_del_archivo>"
  fi
done < "$LINKS_FILE"

echo

echo "Descargas finalizadas. Archivos en: $OUTDIR"
