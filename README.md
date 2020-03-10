# monitoring

Detta Python-projekt hämtar sensordata från GPIO och loggar resultatet i en PostgreSQL-databas.

## Användning

### Utför mätning och loggning med nuvarande användare

`run.sh`

### Utför mätning och loggning med monitoring-användare

`runas.sh`

Om *monitoring*-användaren inte finns, skapa (med hemkatalog):

`sudo useradd --system --create-home monitoring`

## Konfiguration

### Schemaläggning

1. Logga in som användaren som ska köra skriptet
  `sudo su - [user]`
2. Starta crontab `crontab -e`
3. Lägg till en rad för skriptet
    `*/30 * * * * /bin/bash -c "/opt/monitoring/run.sh"` # Kör skriptet var 30:e minut

### Databas-användare

Skapa en fil med namnet `.pgpass` i hemkatalogen för användaren som ska köra skriptet.

`touch $HOME/.pgpass && chmod 600 $HOME/.pgpass`

Lägg till en rad med följande struktur:

`[host]:[port]:[databas]:[användare]:[lösenord]`
