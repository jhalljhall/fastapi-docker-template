# Use the official Ubuntu base image
FROM ubuntu:latest

# Set environment variables to non-interactive (this prevents some prompts)
ENV DEBIAN_FRONTEND=noninteractive

# Install Python and PostgreSQL
RUN apt-get update && \
    apt-get install -y python3 python3-pip postgresql postgresql-contrib

# Set up the PostgreSQL database
USER postgres
RUN    /etc/init.d/postgresql start &&\
    psql --command "CREATE USER postgres WITH SUPERUSER PASSWORD 'postgres';" &&\
    createdb -O postgres postgres

# Allow external connections to PostgreSQL
USER root
RUN echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/*/main/pg_hba.conf
RUN echo "listen_addresses='*'" >> /etc/postgresql/*/main/postgresql.conf

# Expose the PostgreSQL port
EXPOSE 5432

# Copy the requirements.txt file into the container
COPY requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt

# Set up a volume for persistent data
VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]

# Add a script to start the services
COPY start.sh /start.sh
RUN chmod +x /start.sh

# Set the default command to execute
CMD ["/start.sh"]
