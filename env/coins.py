


class Berycoin(Coin):
    NAME = "Berycoin"
    SHORTNAME = "BERY"
    NET = "mainnet"
    XPUB_VERBYTES = bytes.fromhex("0586c22e")
    XPRV_VERBYTES = bytes.fromhex("0586dcf1")
    P2PKH_VERBYTE = bytes.fromhex("19")
    P2SH_VERBYTES = [bytes.fromhex("33"), bytes.fromhex("14")]
    WIF_BYTE = bytes.fromhex("d8")
    GENESIS_HASH = ('ff23a3590cc6e308f1817283cfa80779'
                    '3aae41d6a1de9f30ed15b7e8361d7005')
    DESERIALIZER = lib_tx.DeserializerSegWit
    TX_COUNT = 26906
    TX_COUNT_HEIGHT = 24916
    TX_PER_BLOCK = 10
    RPC_PORT = 9432
    REORG_LIMIT = 800
    PEERS = [
        'electrum.berycoin.com s t',
        'electrum.resteemexposure.com s t',
        'electrum2.berycoin.com s t',        
    ]

#    @classmethod
#    def header_hash(cls, header):
#        '''Given a header return the hash.'''
#        if cls.HEADER_HASH is None:
#            import scrypt
#            cls.HEADER_HASH = lambda x: scrypt.hash(x, x, 1024, 1, 1, 32)

#        version, = struct.unpack('<I', header[:4])
#        if version > 6:
#            return super().header_hash(header)
#        else:
#            return cls.HEADER_HASH(header);


class BerycoinTestnet(Berycoin):
    SHORTNAME = "XBR"
    NET = "testnet"
    XPUB_VERBYTES = bytes.fromhex("053782bf")
    XPRV_VERBYTES = bytes.fromhex("053784a4")
    P2PKH_VERBYTE = bytes.fromhex("0b")
    P2SH_VERBYTES = [bytes.fromhex("3a"), bytes.fromhex("6a")]
    WIF_BYTE = bytes.fromhex("e5")
    GENESIS_HASH = ('fa211189d78247c5173828cdf035a808'
                    'a69d74294022d0d5d170d707544d7ba8')
    TX_COUNT = 1
    TX_COUNT_HEIGHT = 1
    TX_PER_BLOCK = 2
    RPC_PORT = 19432
    REORG_LIMIT = 4000
    PEER_DEFAULT_PORTS = {'t': '51001', 's': '51002'}
    PEERS = [
        'electrum.berycoin.com s t',
        'electrum.resteemexposure.com s t',
    ]
