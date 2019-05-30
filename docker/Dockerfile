FROM python:3.7-slim

# setup uig and gid to 2000. This is mostly done so that derived images, like docker-ds, can use
# 1000 which is commonly the UID of the person running the container in Resero environments and
# when mounting a host directory into the container, allows for appropriate file access, etc.
RUN groupadd --gid 2000 node \
  && useradd --uid 2000 --gid node --shell /bin/bash --create-home node

ENV NODE_VERSION 8.15.1

# workaround for issue where gpg reports "keyserver received failed: Cannot assign requested address"
# see: https://github.com/inversepath/usbarmory-debian-base_image/issues/9
RUN mkdir ~/.gnupg; \
    chmod 600 ~/.gnupg; \
    echo "disable-ipv6" >> ~/.gnupg/dirmngr.conf

RUN set -ex; \
    buildDeps='xz-utils' \
    && ARCH= && dpkgArch="$(dpkg --print-architecture)" \
    && case "${dpkgArch##*-}" in \
      amd64) ARCH='x64';; \
      ppc64el) ARCH='ppc64le';; \
      s390x) ARCH='s390x';; \
      arm64) ARCH='arm64';; \
      armhf) ARCH='armv7l';; \
      i386) ARCH='x86';; \
      *) echo "unsupported architecture"; exit 1 ;; \
    esac \
    && set -ex \
    && apt-get update && apt-get install -y ca-certificates curl wget gnupg dirmngr $buildDeps --no-install-recommends \
    && rm -rf /var/lib/apt/lists/* \
    && for key in \
      94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \
      FD3A5288F042B6850C66B31F09FE44734EB7990E \
      71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \
      DD8F2338BAE7501E3DD5AC78C273792F7D83545D \
      C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \
      B9AE9905FFD7803F25714661B63B535A4C206CA9 \
      77984A986EBC2AA786BC0F66B01FBB92821C587A \
      8FCCA13FEF1D0C2E91008E09770F7A9A5AE15600 \
      4ED778F539E3634C779C87C6D7062848A1AB005C \
      A48C2BEE680E841632CD4E44F07496B3EB3C1762 \
      B9E2F5981AA6E0CD28160D9FF13993A75599653C \
    ; do \
      gpg --batch --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys "$key" || \
      gpg --batch --keyserver hkp://ipv4.pool.sks-keyservers.net --recv-keys "$key" || \
      gpg --batch --keyserver hkp://pgp.mit.edu:80 --recv-keys "$key" ; \
    done \
    && curl -fsSLO --compressed "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-$ARCH.tar.xz" \
    && curl -fsSLO --compressed "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \
    && gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \
    && grep " node-v$NODE_VERSION-linux-$ARCH.tar.xz\$" SHASUMS256.txt | sha256sum -c - \
    && tar -xJf "node-v$NODE_VERSION-linux-$ARCH.tar.xz" -C /usr/local --strip-components=1 --no-same-owner \
    && rm "node-v$NODE_VERSION-linux-$ARCH.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt \
    && apt-get purge -y --auto-remove $buildDeps \
    && ln -s /usr/local/bin/node /usr/local/bin/nodejs

ENV YARN_VERSION 1.12.3

RUN set -ex \
  && for key in \
    6A010C5166006599AA17F08146C2130DFD2497F5 \
  ; do \
    gpg --batch --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys "$key" || \
    gpg --batch --keyserver hkp://ipv4.pool.sks-keyservers.net --recv-keys "$key" || \
    gpg --batch --keyserver hkp://pgp.mit.edu:80 --recv-keys "$key" ; \
  done \
  && curl -fsSLO --compressed "https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz" \
  && curl -fsSLO --compressed "https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz.asc" \
  && gpg --batch --verify yarn-v$YARN_VERSION.tar.gz.asc yarn-v$YARN_VERSION.tar.gz \
  && mkdir -p /opt \
  && tar -xzf yarn-v$YARN_VERSION.tar.gz -C /opt/ \
  && ln -s /opt/yarn-v$YARN_VERSION/bin/yarn /usr/local/bin/yarn \
  && ln -s /opt/yarn-v$YARN_VERSION/bin/yarnpkg /usr/local/bin/yarnpkg \
&& rm yarn-v$YARN_VERSION.tar.gz.asc yarn-v$YARN_VERSION.tar.gz

# COPY ./docker_entrypoint.sh /
# CMD []
# ENTRYPOINT ["/docker_entrypoint.sh"]

# RUN printf "deb http://archive.debian.org/debian/ jessie main\ndeb-src http://archive.debian.org/debian/ jessie main\ndeb http://security.debian.org jessie/updates main\ndeb-src http://security.debian.org jessie/updates main" > /etc/apt/sources.list
RUN apt-get update && apt-get install build-essential --allow-unauthenticated -y && pip install Cython
RUN apt-get install libpng-dev --allow-unauthenticated -y
RUN apt-get install libfreetype6-dev --allow-unauthenticated -y
RUN apt-get install libgomp1 --allow-unauthenticated -y
RUN apt-get install libjpeg-dev --allow-unauthenticated -y
RUN apt-get install libfreetype6-dev --allow-unauthenticated -y
RUN apt-get install libfreetype6-dev --allow-unauthenticated -y
RUN ln -s /usr/lib/i386-linux-gnu/libfreetype.so /usr/lib
RUN ln -s /usr/lib/i386-linux-gnu/libjpeg.so /usr/lib
RUN ln -s /usr/lib/i386-linux-gnu/libz.so /usr/lib


COPY docker/root/tmp/requirements.txt /tmp/requirements.txt

RUN cd /tmp; \
    pip install --no-cache-dir -r requirements.txt

RUN jupyter serverextension enable --py jupyterlab \
    && jupyter nbextension enable --py widgetsnbextension \
    && jupyter labextension install \
        @jupyter-widgets/jupyterlab-manager \
        jupyter-matplotlib \
        jupyterlab_bokeh \
        @pyviz/jupyterlab_pyviz \
        @jupyterlab/plotly-extension \
        @mflevine/jupyterlab_html

#
# Configure environment
#
# Use 1000 for uid and gid. It's common in the docker environments for a host directory to be mounted
# into the container, when this is done, it's also common for the uid/gid of the user doing so to be
# 1000. This allows for "correct" file privileges when doing so
# Change the NB_USER value to match your custom username.
ENV NB_USER=spendyala \
    NB_UID=1000 \
    NB_GID=1000

# assumes that the project has been mounted into /home/$NB_USER/project
# to ensure this derived projects should add the following to their dockerutils.cfg file
# [notebook]
# volumes=--mount type=bind,source={project_root},target=/home/$NB_USER/project

RUN useradd -m -s /bin/bash -N -u $NB_UID $NB_USER

RUN set -ex; \
    apt-get update; \
    apt-get install -y \
        less \
        vim \
    ; \
    apt-get clean; \
    rm -rf /var/tmp/* /tmp/* /var/lib/apt/lists/*

COPY docker/root/ /


ADD docker/jupyter_notebook_config.py /home/$NB_USER/.jupyter/jupyter_notebook_config.py
RUN chown -R $NB_USER /home/$NB_USER/.jupyter; \
    usermod -u 2005 node; \
    groupmod -g 2005 node; \
    usermod -u 1000 $NB_USER

# RUN mkdir -p /home/$NB_USER/mnist; \
#     cd /home/$NB_USER/mnist; \
#     wget -q https://s3-bucket-files; \
#     gunzip *.gz

RUN echo NOTEBOOK_USER=$NB_USER > /etc/environment
CMD ["/usr/local/bin/start-notebook.sh"]
ENTRYPOINT ["/docker-entrypoint.sh"]
