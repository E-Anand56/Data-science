class univariate():
    def quanqual(data):
        qual=[]
        quan=[]
        for column in data.columns:
            #print(column)
            if data[column].dtype == "object":        
                #print("qual")
                qual.append(column)
            else:
                quan.append(column)
                #print("qual")
        return quan,qual
    