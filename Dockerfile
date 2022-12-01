FROM btces/ep
  
USER 0
WORKDIR e
RUN mkdir -p e/Reports

COPY . e




