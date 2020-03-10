# monitoring

Detta Python-projekt hämtar sensordata från GPIO och loggar resultatet i en PostgreSQL-databas.

## Användning

### Utför mätning och loggning med nuvarande användare

`run.sh`

### Utför mätning och loggning med monitoring-användare

`runas.sh`

Om *monitoring*-användaren inte finns, skapa (med hemkatalog):

`sudo useradd --system --create-home monitoring`

## Databaskonfiguration

### Användare

Skapa en fil med namnet `.pgpass` i hemkatalogen för användaren som ska köra skriptet.

`touch $HOME/.pgpass && chmod 600 $HOME/.pgpass`

Lägg till en rad med följande struktur:

`[host]:[port]:[databas]:[användare]:[lösenord]`
