## Usage

### 1.
```
apt-get update \
    && apt-get install -y cron screen nano build-essential libtool autotools-dev automake pkg-config libssl-dev libevent-dev bsdmainutils \
    && apt-get install -y libboost-system-dev libboost-filesystem-dev libboost-chrono-dev libboost-program-options-dev libboost-test-dev libboost-thread-dev libboost-all-dev software-properties-common  \
    && add-apt-repository -y ppa:bitcoin/bitcoin \
    && apt-get update \
    && apt-get install -y libdb4.8-dev libdb4.8++-dev libminiupnpc-dev libzmq3-dev libqrencode-dev letsencrypt \
    && apt-get clean \
    && mkdir -p /ssl \
```

### 2.
```
    openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /ssl/privkey.pem -out /ssl/cert.pem -subj /CN=electrum.berycoin.com \    

```

### 3.
```
    add-apt-repository -y ppa:jonathonf/python-3.6 \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
       python3.6 python3.6-dev libleveldb-dev wget git libssl-dev daemontools nano build-essential \
    && rm /usr/bin/python3 \
    && ln -s /usr/bin/python3.6 /usr/bin/python3 \
    && wget https://bootstrap.pypa.io/get-pip.py -O- | python3.6 \
    && pip install scrypt \
    && apt-get clean \
    && mkdir /log /db /env \
    && groupadd -r electrumx \
    && useradd -s /bin/bash -m -g electrumx electrumx \
    && sudo usermod -a -G sudo electrumx \
    && chown -R electrumx:electrumx /ssl \
    && cd /home/electrumx \
    && git clone https://github.com/berycoin-project/berycoin.git \
    && chown -R electrumx:electrumx berycoin \
    && mkdir /home/electrumx/.berycoin \
    && cd /home/electrumx \
    && chown -R electrumx:electrumx .berycoin \
    && git clone https://github.com/berycoin-project/electrumx.git \
    && chown -R electrumx:electrumx electrumx && cd electrumx \
    && chown -R electrumx:electrumx /log /db /env \
    && python3.6 setup.py install
```

### 4.
```
touch /var/log/cron.log \
    && chown -R electrumx:electrumx /var/log/cron.log
```

### 5.
```
passwd electrumx

```

### 6.
```
su electrumx
```

### 7.
```
cd /home/electrumx \
 && git clone https://github.com/Bago213/Electrumx-guide \
 && cd Electrumx-guide
 
```

### 8.
Edit `env/HOST` to your coin.

Edit `env/REPORT_HOST` to your coin.

Edit `env/DAEMON_URL` accordingly.Need to match your daemon.

Edit `berycoin/berycoin.conf` accordingly.Need to match your RPCuser & RPCpassword in env/DAEMON_URL.


### 9.
```
cp -R env/* /env/ \
 && cp -R berycoin/* /home/electrumx/.berycoin/ 
```

### 10.
```
cd ~ \
    && cd /home/electrumx/berycoin \
    && git checkout 0.16 \
    && /home/electrumx/berycoin/autogen.sh \
    && /home/electrumx/berycoin/configure \
    && make -j4 \
    && cd ~ \
    && mkdir -p ~/service ~/scripts/electrumx \
    && cp -R ~/electrumx/contrib/daemontools/* ~/scripts/electrumx \
    && chmod +x ~/scripts/electrumx/run \
    && chmod +x ~/scripts/electrumx/log/run \
    && sed -i '$d' ~/scripts/electrumx/log/run \
    && sed -i '$a\exec multilog t s500000 n10 /log' ~/scripts/electrumx/log/run  \
    && cp /env/* /home/electrumx/scripts/electrumx/env/ \
    && cat ~/scripts/electrumx/env/coins.py >> ~/electrumx/lib/coins.py \
    && ln -s ~/scripts/electrumx  ~/service/electrumx
```

### 11.
```
cron && tail -f /var/log/cron.log
```

### 12.
```
/home/electrumx/berycoin/src/berycoind &
```

### 13.
```
cp /env/* /home/electrumx/scripts/electrumx/env/ && svscan ~/service

svscan ~/service & disown
```

### 14. access logs.
```
tail -F /log/current | tai64nlocal
```

### 15. terminate electrum
```
svc -d ~/service/electrumx
```

### 16. status electrum
```
svstat ~/service/electrumx
```

### 17. start electrum
```
svc -u ~/service/electrumx
```

