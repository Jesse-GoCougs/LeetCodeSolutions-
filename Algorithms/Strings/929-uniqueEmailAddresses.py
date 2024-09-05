# class Solution(object):
#     def numUniqueEmails(self, emails):
#         """
#         :type emails: List[str]
#         :rtype: int
#         """
#         validEmails = set()

#         for email in emails:
#             i, local = 0, ""
#             while email[i] not in ["@", "+"]:
#                 if email[i] != ".":
#                     local += email[i]
#                 i+=1
#             while email[i] != "@":
#                 i+=1
#             domain = email[i+1:]
#             validEmails.add((local, domain))
#         return len(validEmails)

class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        validEmails = set()

        for email in emails:
            local, domain = email.split("@")
            local = local.split("+")[0]
            local = local.replace(".", "")
            validEmails.add((local, domain))
        return len(validEmails)
