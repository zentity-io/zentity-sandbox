FROM docker.elastic.co/elasticsearch/elasticsearch:8.13.3

# Copy zentity sandbox indices from local directory
COPY ./esdata/indices/HUT00XIcTVGLCV1pual-Dg /usr/share/elasticsearch/data/indices/HUT00XIcTVGLCV1pual-Dg
COPY ./esdata/indices/A9Bp_BvkSIirvH__x5L9wg /usr/share/elasticsearch/data/indices/A9Bp_BvkSIirvH__x5L9wg
COPY ./esdata/indices/SsUdwK6iSNOhMsKbWj8Qnw /usr/share/elasticsearch/data/indices/SsUdwK6iSNOhMsKbWj8Qnw
COPY ./esdata/indices/LK6Mc4KnT4C4qR5VfarjlA /usr/share/elasticsearch/data/indices/LK6Mc4KnT4C4qR5VfarjlA
COPY ./esdata/indices/V-8xJG3rQw2s_VowcoGi5A /usr/share/elasticsearch/data/indices/V-8xJG3rQw2s_VowcoGi5A
COPY ./esdata/indices/f4vZIHGCTa67T-gyg1JPAA /usr/share/elasticsearch/data/indices/f4vZIHGCTa67T-gyg1JPAA
COPY ./esdata/indices/mppvFcMyQoCi74VKKkY1Pg /usr/share/elasticsearch/data/indices/mppvFcMyQoCi74VKKkY1Pg
COPY ./esdata/indices/vau_RM-kQYqd6177R_8mig /usr/share/elasticsearch/data/indices/vau_RM-kQYqd6177R_8mig
COPY ./esdata/indices/sya5QhLoTZyjt9NUtC6WmQ /usr/share/elasticsearch/data/indices/sya5QhLoTZyjt9NUtC6WmQ
COPY ./esdata/indices/m7LbnKBsSrKayF60QDoAzA /usr/share/elasticsearch/data/indices/m7LbnKBsSrKayF60QDoAzA
COPY ./esdata/indices/Cbcfrp4rQ16828Wd5bzJtA /usr/share/elasticsearch/data/indices/Cbcfrp4rQ16828Wd5bzJtA
COPY ./esdata/indices/1hMreHfXR76sxsUAfcmzDA /usr/share/elasticsearch/data/indices/1hMreHfXR76sxsUAfcmzDA
COPY ./esdata/indices/Zphnd57mRAaVerFQe2HrOg /usr/share/elasticsearch/data/indices/Zphnd57mRAaVerFQe2HrOg

# Set permissions to that of elasticsearch image
USER root
RUN chmod -R 0775 /usr/share/elasticsearch/data/indices
RUN chown -R elasticsearch /usr/share/elasticsearch/data/indices

# Install plugins
USER elasticsearch
RUN elasticsearch-plugin install --batch https://zentity.io/releases/zentity-1.8.3-elasticsearch-8.13.3.zip
RUN elasticsearch-plugin install --batch analysis-icu
RUN elasticsearch-plugin install --batch analysis-phonetic

# Use entrypoint from elasticsearch image
ENTRYPOINT ["/bin/tini", "--", "/usr/local/bin/docker-entrypoint.sh"]