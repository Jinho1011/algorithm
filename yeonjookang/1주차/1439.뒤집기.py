import sys
S=sys.stdin.readline().rstrip()

seq_1=0
seq_0=0

for i in range(len(S)-1):
    if S[i]=='0' and S[i]!=S[i+1]:
        seq_0+=1
    elif S[i]=='1' and S[i]!=S[i+1]:
        seq_1+=1
    
#마지막 수 고려
if S[len(S)-1]=='0' : seq_0+=1
else : seq_1+=1

print(min(seq_0,seq_1))
    
        
