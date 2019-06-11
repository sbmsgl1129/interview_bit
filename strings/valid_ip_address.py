class Solution:
    # @param A : string
    # @return a list of strings
    def restoreIpAddresses(self, A):
        
        size = len(A)
        if size < 4 or size > 12:
            return []
        
        return self.listAddresses(A, 4)
    
    def listAddresses(self, address_string, num_octets):
        address_list = []
        
        if len(address_string) == 0:
            return address_list #Its empty here
        
        if num_octets == 1:
            if len(address_string) < 1 or len(address_string) > 3:
                return address_list #It is empty here
            
            if len(address_string) !=  1 and address_string[0] == '0':
                return address_list #It is empty here
            
            if len(address_string) == 3 and int(address_string) > 255:
                return address_list #It is empty here
            
            address_list.append(address_string)
            return address_list
        
        size  = len(address_string)
        
        #Taking one char for this octet
        if size >= 1:
            remaining_octets = self.listAddresses(address_string[1:],num_octets - 1)
            if remaining_octets:
                address_list.extend([address_string[0:1] + '.' + remaining_octet for remaining_octet in remaining_octets])
        
        #Taking two chars for this octet
        if size >= 2 and address_string[0] != '0':
            remaining_octets = self.listAddresses(address_string[2:],num_octets - 1)
            if remaining_octets:
                address_list.extend([address_string[0:2] + '.' + remaining_octet for remaining_octet in remaining_octets])
        
        #Taking three chars for this octet
        if size >= 3 and address_string[0] != '0' and int(address_string[0:3]) <= 255:
            remaining_octets = self.listAddresses(address_string[3:],num_octets - 1)
            if remaining_octets:
                address_list.extend([address_string[0:3] + '.' + remaining_octet for remaining_octet in remaining_octets])        
        
        #print(address_list)
        return address_list
