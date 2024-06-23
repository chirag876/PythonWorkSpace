class Calculatenetpremium:
    def __init__(self):
        self.net_premium = 0
        self.gross_comm_amt = 0
        self.broker_fee = 0
        self.broker_insp_fee = 0
        self.other_fee_amount = 0
        self.total_inv_fee = 0
        self.total_inv_taxes =0

    def calculate(self,source_df):
        # Assuming 'Premium' and 'Commission amount' are keys in the mapping
        net_premium_count = []
        for i in range(len(source_df)):
            gross_premium = source_df['Gross Premium'][i]
            gross_comm_amt = source_df['Gross Comm Amt'][i]
            broker_fee = source_df['Broker Fee'][i]
            broker_insp_fee = source_df['Broker Insp Fee'][i]
            other_fee_amount = '$0,.0'
            if(source_df['Other Fee Amount'][i] is not None):
                other_fee_amount = source_df['Other Fee Amount'][i] 
            total_inv_fee = '$0,.0'         
            if(source_df['Total INV Fees'][i] is not None):
                total_inv_fee = source_df['Total INV Fees'][i]
            total_inv_taxes = '$0,.0'          
            if(source_df['Total INV Taxes'][i] is not None):
                total_inv_taxes = source_df['Total INV Taxes'][i]
            
       
        # Perform the calculation (addition in this case)
            gross_premium = gross_premium.replace('$', '').replace(' ', '').replace(',', '').replace('(', '').replace(')', '')
            gross_comm_amt = gross_comm_amt.replace('$', '').replace(' ', '').replace(',', '').replace('(', '').replace(')', '')
            broker_fee = broker_fee.replace('$', '').replace(' ', '').replace(',', '').replace('(', '').replace(')', '')
            broker_insp_fee = broker_insp_fee.replace('$', '').replace(' ', '').replace(',', '').replace('(', '').replace(')', '')
            other_fee_amount = other_fee_amount.replace('$', '').replace(' ', '').replace(',', '').replace('(', '').replace(')', '')
            total_inv_fee = total_inv_fee.replace('$', '').replace(' ', '').replace(',', '').replace('(', '').replace(')', '')
            total_inv_taxes = total_inv_taxes.replace('$', '').replace(' ', '').replace(',', '').replace('(', '').replace(')', '')
            net_premium = ((float(gross_premium) - float(gross_comm_amt))+float(broker_fee) +float(other_fee_amount)+ float(total_inv_fee) + float(total_inv_taxes) )
            net_premium_count.append(net_premium)
           
        return net_premium_count
    
    
    

    
    

   
