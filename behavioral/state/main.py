from modules.context import Invoice

    
if __name__ == '__main__':
    invoice = Invoice()
    
    invoice.emit()
    print('Emit date:',invoice.emit_date)
    print('#######')
    
    invoice.pending()
    print('#####')
    
    invoice.cancel()
    print('Cancelation date:',invoice.emit_date)