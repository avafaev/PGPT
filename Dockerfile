FROM kalilinux/kali-rolling

WORKDIR /app

# Instalar las dependencias necesarias incluyendo sudo
RUN apt-get update && apt-get install -y \
    dnsutils \
    nmap \
    sqlmap \
    curl \
    git \
    python3-pip \
    sudo \
    hydra \
    sublist3r \
    dirb \
    gobuster \
    aircrack-ng \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Crear un nuevo usuario con privilegios sudo
RUN useradd -m -s /bin/bash pentester && echo "pentester:pentester" | chpasswd && adduser pentester sudo

# Dar permisos de sudo sin contraseña al usuario
RUN echo "pentester ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

RUN chown -R pentester:pentester /app

RUN pip3 install --ignore-installed git+https://github.com/TomasBastanteFlor/PGPT

RUN git clone --filter=blob:none --sparse https://github.com/TomasBastanteFlor/PGPT.git && \
    cd PGPT && \
    git sparse-checkout init --cone && \
    git sparse-checkout set lists && \
    mkdir -p /usr/share/wordlists/dirbuster && \
    mv lists/* /usr/share/wordlists/dirbuster/ && \
    cd .. && \
    rm -rf PGPT

# Copiar los archivos de la aplicación al contenedor
COPY . .

# Agregar el mensaje de aviso al bashrc del usuario pentester
RUN echo 'echo "Please set your OpenAI API Key using: export OPENAI_API_KEY=<your key here>"' >> /home/pentester/.bashrc

# Exponer el puerto 8000
EXPOSE 8000

# Cambiar al usuario pentester
USER pentester

# Comando por defecto
CMD ["bash"]