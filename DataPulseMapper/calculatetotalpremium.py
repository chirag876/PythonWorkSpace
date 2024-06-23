class Calculatetotalpremium:
    def __init__(self):
        self.net_premium = 0
        self.gross_comm_amt = 0
        self.broker_fee = 0
        self.broker_insp_fee = 0
        self.other_fee_amount = 0
        self.total_inv_fee = 0
        self.total_inv_taxes =0

    def calculate(self,source_df):
        net_premium_count = []
        for i in range(len(source_df)):
            gross_premium = source_df['Gross Premium'][i]
            gross_comm_amt = source_df['Gross Comm Amt'][i]
    
        # Perform the calculation (addition in this case)
            gross_premium = gross_premium.replace('$', '').replace(' ', '').replace(',', '').replace('(', '').replace(')', '')
            gross_comm_amt = gross_comm_amt.replace('$', '').replace(' ', '').replace(',', '').replace('(', '').replace(')', '')
            net_premium = (float(gross_premium) + float(gross_comm_amt))
            net_premium_count.append(net_premium)
              
        return net_premium_count

    

    
    

   
