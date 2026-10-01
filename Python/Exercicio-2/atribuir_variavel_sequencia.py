preproInsulin = (
    "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpkt"
    "rreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"
)

lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslq"
aInsulin = "krgiveqcctsicslyqlenycn"

insulin = lsInsulin + bInsulin + cInsulin + aInsulin

print(insulin)
print(preproInsulin)
print("Sequência da cadeia A: " + aInsulin)

realMolecularWeight = 5807.63
molecularWeightInsulin = 5807.63

percentualErro = (
    abs(molecularWeightInsulin - realMolecularWeight)
    / realMolecularWeight
) * 100

print(f"Percentual de erro: {percentualErro:.2f}%")