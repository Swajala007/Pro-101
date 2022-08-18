import dropbox

class Transferdata:
    def __init__(self,accesstoken):
        self.accesstoken = accesstoken

    def uploadFiles(self,filefrom,fileto):
        dbx = dropbox.Dropbox(self.accesstoken)
        with open(filefrom,"rb") as f:
            dbx.files_upload(f.read(),fileto)


def main():
    accesstoken="sl.BNF9IAMtnZnKU1j-VTq4dhHpTtjH_0dldx_U8O-w_xk6PmnhkDWGUwnz_uq5QIZxAPGKzVs61n4Ao934CLBWKz3qDO71fckW8-SW34RAIDx9HcMLMyAh9RmIGNqdqk-_byOmG2mj0nf-"
    transferdata = Transferdata(accesstoken)

    filefrom = "write.txt"
    fileto ="/newfolder/text.txt"
    transferdata.uploadFiles(filefrom,fileto)
    print("filesuploaded")

main()    