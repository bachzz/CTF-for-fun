from periodictable import elements

data = "AuAtPbGeLuPbTmTbPoTmBiPoGeFrTmTbRePtTmBiBiGeOsTaTmBiGeTaPtGeLuTaRnTaPtLuGeAtHgPdGePoHfTmGeIrAuBiPoGeHoTmPbPoTbTaPtGeFrTbAcGePoAuGeBiAtHoHoTmTmErGeTaBiGeTbOsFrTbAcBiGePoAuGePoPbAcGeAuPtTmGeIrAuPbTmGePoTaIrTmPdGePoHfTmGeYbOsTbLuGeTaBiGeErAuAcAuAtOsAuRnTmHoHfTmIrTaBiPoPbAcEu"
#for el in elements: 
#	print("%s %s"%(el.symbol,el.number))
for i in range(0, len(data), 2):
	tmp = data[i:i+2]	
	for el in elements:
		if tmp==el.symbol:
			print el.number,
