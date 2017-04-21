#!/usr/bin/python
#################
#
#   This is a code snippet ( something I do often with python ) that contains itertools product functions
#   using several sets of characters. Standard characters not yet included in this set are []`~
#   The point of shifting the character set start positions is so you can execute child processes that
#   write fixed block sizes based on disk space, use the block, then move on to another starting position
#   so you can chunk you way through the entire set, even if you don't have the disk space for the whole set.
#   If you have the disk space, you would use
#gen4()
#gen5()
#gen6()
#gen7()
#gen8()
#gen9()
#gen10()
#gen11()
#gen12()
#
#   to generate all combinations of the characters for 4,5,6,7,8,9,10,11, and 12 character length strings.
#
#
#################
import itertools

res4 = itertools.product('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|', repeat=4)
res5 = itertools.product('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|', repeat=5)
res6 = itertools.product('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|', repeat=6)

res7 = itertools.product('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|', repeat=7)
res8 = itertools.product('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|', repeat=8)
res9 = itertools.product('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|', repeat=9)
res10 = itertools.product('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|', repeat=10)
res11 = itertools.product('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|', repeat=11)
res12 = itertools.product('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|', repeat=12)

res13 = itertools.product('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=4)
res14 = itertools.product('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=5)
res15 = itertools.product('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=6)
res16 = itertools.product('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=7)
res17 = itertools.product('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=8)
res18 = itertools.product('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=9)
res19 = itertools.product('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=10)
res20 = itertools.product('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=11)
res21 = itertools.product('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=12)

res22 = itertools.product('bcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZa', repeat=4)
res23 = itertools.product('cdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZab', repeat=4)
res24 = itertools.product('defghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabc', repeat=4)
res25 = itertools.product('efghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcd', repeat=4)
res26 = itertools.product('fghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcde', repeat=4)
res27 = itertools.product('ghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdef', repeat=4)
res28 = itertools.product('hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefg', repeat=4)
res29 = itertools.product('ijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefgh', repeat=4)
res30 = itertools.product('jklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgi', repeat=4)
res31 = itertools.product('klmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgij', repeat=4)
res32 = itertools.product('lmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijk', repeat=4)
res33 = itertools.product('mnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijkl', repeat=4)
res34 = itertools.product('nopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklm', repeat=4)
res35 = itertools.product('opqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmn', repeat=4)
res36 = itertools.product('pqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmno', repeat=4)
res37 = itertools.product('qrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnop', repeat=4)
res38 = itertools.product('rstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnop1', repeat=4)
res39 = itertools.product('stuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqr', repeat=4)
res40 = itertools.product('tuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrs', repeat=4)
res41 = itertools.product('uvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrst', repeat=4)
res42 = itertools.product('vwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstu', repeat=4)
res43 = itertools.product('wxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuv', repeat=4)
res44 = itertools.product('xyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvw', repeat=4)
res45 = itertools.product('yzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwx', repeat=4)
res46 = itertools.product('zABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxy', repeat=4)
res47 = itertools.product('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyz', repeat=4)
res48 = itertools.product('BCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzA', repeat=4)
res49 = itertools.product('CDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzAB', repeat=4)
res50 = itertools.product('DEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABC', repeat=4)
res51 = itertools.product('EFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCD', repeat=4)
res52 = itertools.product('FGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDE', repeat=4)
res53 = itertools.product('GHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEF', repeat=4)
res54 = itertools.product('HIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFG', repeat=4)
res55 = itertools.product('IJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGH', repeat=4)
res56 = itertools.product('JKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHI', repeat=4)
res57 = itertools.product('KLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJ', repeat=4)
res58 = itertools.product('LMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJK', repeat=4)
res59 = itertools.product('MNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKL', repeat=4)
res60 = itertools.product('NOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLM', repeat=4)
res61 = itertools.product('OPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN', repeat=4)
res62 = itertools.product('PQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNO', repeat=4)
res63 = itertools.product('QRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP', repeat=4)
res64 = itertools.product('RSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQ', repeat=4)
res65 = itertools.product('STUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR', repeat=4)
res66 = itertools.product('TUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRS', repeat=4)
res67 = itertools.product('UVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRST', repeat=4)
res68 = itertools.product('VWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTU', repeat=4)
res69 = itertools.product('WXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV', repeat=4)
res70 = itertools.product('XYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW', repeat=4)
res71 = itertools.product('YZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWX', repeat=4)
res72 = itertools.product('ZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXY', repeat=4)

res222 = itertools.product('bcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZa', repeat=5)
res223 = itertools.product('cdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZab', repeat=5)
res224 = itertools.product('defghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabc', repeat=5)
res225 = itertools.product('efghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcd', repeat=5)
res226 = itertools.product('fghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcde', repeat=5)
res227 = itertools.product('ghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdef', repeat=5)
res228 = itertools.product('hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefg', repeat=5)
res229 = itertools.product('ijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefgh', repeat=5)
res330 = itertools.product('jklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgi', repeat=5)
res331 = itertools.product('klmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgij', repeat=5)
res332 = itertools.product('lmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijk', repeat=5)
res333 = itertools.product('mnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijkl', repeat=5)
res334 = itertools.product('nopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklm', repeat=5)
res335 = itertools.product('opqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmn', repeat=5)
res336 = itertools.product('pqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmno', repeat=5)
res337 = itertools.product('qrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnop', repeat=5)
res338 = itertools.product('rstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnop1', repeat=5)
res339 = itertools.product('stuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqr', repeat=5)
res440 = itertools.product('tuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrs', repeat=5)
res441 = itertools.product('uvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrst', repeat=5)
res442 = itertools.product('vwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstu', repeat=5)
res443 = itertools.product('wxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuv', repeat=5)
res444 = itertools.product('xyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvw', repeat=5)
res445 = itertools.product('yzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwx', repeat=5)
res446 = itertools.product('zABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxy', repeat=5)
res447 = itertools.product('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyz', repeat=5)
res448 = itertools.product('BCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzA', repeat=5)
res449 = itertools.product('CDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzAB', repeat=5)
res550 = itertools.product('DEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABC', repeat=5)
res551 = itertools.product('EFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCD', repeat=5)
res552 = itertools.product('FGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDE', repeat=5)
res553 = itertools.product('GHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEF', repeat=5)
res554 = itertools.product('HIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFG', repeat=5)
res555 = itertools.product('IJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGH', repeat=5)
res556 = itertools.product('JKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHI', repeat=5)
res557 = itertools.product('KLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJ', repeat=5)
res558 = itertools.product('LMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJK', repeat=5)
res559 = itertools.product('MNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKL', repeat=5)
res660 = itertools.product('NOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLM', repeat=5)
res661 = itertools.product('OPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN', repeat=5)
res662 = itertools.product('PQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNO', repeat=5)
res663 = itertools.product('QRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP', repeat=5)
res664 = itertools.product('RSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQ', repeat=5)
res665 = itertools.product('STUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR', repeat=5)
res666 = itertools.product('TUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRS', repeat=5)
res667 = itertools.product('UVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRST', repeat=5)
res668 = itertools.product('VWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTU', repeat=5)
res669 = itertools.product('WXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV', repeat=5)
res770 = itertools.product('XYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW', repeat=5)
res771 = itertools.product('YZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWX', repeat=5)
res772 = itertools.product('ZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXY', repeat=5)

res2222 = itertools.product('bcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZa', repeat=6)
res2223 = itertools.product('cdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZab', repeat=6)
res2224 = itertools.product('defghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabc', repeat=6)
res2225 = itertools.product('efghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcd', repeat=6)
res2226 = itertools.product('fghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcde', repeat=6)
res2227 = itertools.product('ghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdef', repeat=6)
res2228 = itertools.product('hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefg', repeat=6)
res2229 = itertools.product('ijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefgh', repeat=6)
res3330 = itertools.product('jklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgi', repeat=6)
res3331 = itertools.product('klmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgij', repeat=6)
res3332 = itertools.product('lmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijk', repeat=6)
res3333 = itertools.product('mnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijkl', repeat=6)
res3334 = itertools.product('nopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklm', repeat=6)
res3335 = itertools.product('opqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmn', repeat=6)
res3336 = itertools.product('pqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmno', repeat=6)
res3337 = itertools.product('qrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnop', repeat=6)
res3338 = itertools.product('rstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnop1', repeat=6)
res3339 = itertools.product('stuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqr', repeat=6)
res4440 = itertools.product('tuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrs', repeat=6)
res4441 = itertools.product('uvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrst', repeat=6)
res4442 = itertools.product('vwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstu', repeat=6)
res4443 = itertools.product('wxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuv', repeat=6)
res4444 = itertools.product('xyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvw', repeat=6)
res4445 = itertools.product('yzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwx', repeat=6)
res4446 = itertools.product('zABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxy', repeat=6)
res4447 = itertools.product('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyz', repeat=6)
res4448 = itertools.product('BCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzA', repeat=6)
res4449 = itertools.product('CDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzAB', repeat=6)
res5550 = itertools.product('DEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABC', repeat=6)
res5551 = itertools.product('EFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCD', repeat=6)
res5552 = itertools.product('FGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDE', repeat=6)
res5553 = itertools.product('GHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEF', repeat=6)
res5554 = itertools.product('HIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFG', repeat=6)
res5555 = itertools.product('IJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGH', repeat=6)
res5556 = itertools.product('JKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHI', repeat=6)
res5557 = itertools.product('KLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJ', repeat=6)
res5558 = itertools.product('LMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJK', repeat=6)
res5559 = itertools.product('MNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKL', repeat=6)
res6660 = itertools.product('NOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLM', repeat=6)
res6661 = itertools.product('OPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN', repeat=6)
res6662 = itertools.product('PQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNO', repeat=6)
res6663 = itertools.product('QRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP', repeat=6)
res6664 = itertools.product('RSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQ', repeat=6)
res6665 = itertools.product('STUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR', repeat=6)
res6666 = itertools.product('TUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRS', repeat=6)
res6667 = itertools.product('UVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRST', repeat=6)
res6668 = itertools.product('VWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTU', repeat=6)
res6669 = itertools.product('WXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV', repeat=6)
res7770 = itertools.product('XYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW', repeat=6)
res7771 = itertools.product('YZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWX', repeat=6)
res7772 = itertools.product('ZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXY', repeat=6)

res22222 = itertools.product('bcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZa', repeat=7)
res22223 = itertools.product('cdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZab', repeat=7)
res22224 = itertools.product('defghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabc', repeat=7)
res22225 = itertools.product('efghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcd', repeat=7)
res22226 = itertools.product('fghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcde', repeat=7)
res22227 = itertools.product('ghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdef', repeat=7)
res22228 = itertools.product('hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefg', repeat=7)
res22229 = itertools.product('ijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefgh', repeat=7)
res33330 = itertools.product('jklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgi', repeat=7)
res33331 = itertools.product('klmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgij', repeat=7)
res33332 = itertools.product('lmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijk', repeat=7)
res33333 = itertools.product('mnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijkl', repeat=7)
res33334 = itertools.product('nopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklm', repeat=7)
res33335 = itertools.product('opqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmn', repeat=7)
res33336 = itertools.product('pqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmno', repeat=7)
res33337 = itertools.product('qrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnop', repeat=7)
res33338 = itertools.product('rstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnop1', repeat=7)
res33339 = itertools.product('stuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqr', repeat=7)
res44440 = itertools.product('tuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrs', repeat=7)
res44441 = itertools.product('uvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrst', repeat=7)
res44442 = itertools.product('vwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstu', repeat=7)
res44443 = itertools.product('wxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuv', repeat=7)
res44444 = itertools.product('xyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvw', repeat=7)
res44445 = itertools.product('yzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwx', repeat=7)
res44446 = itertools.product('zABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxy', repeat=7)
res44447 = itertools.product('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyz', repeat=7)
res44448 = itertools.product('BCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzA', repeat=7)
res44449 = itertools.product('CDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzAB', repeat=7)
res55550 = itertools.product('DEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABC', repeat=7)
res55551 = itertools.product('EFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCD', repeat=7)
res55552 = itertools.product('FGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDE', repeat=7)
res55553 = itertools.product('GHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEF', repeat=7)
res55554 = itertools.product('HIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFG', repeat=7)
res55555 = itertools.product('IJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGH', repeat=7)
res55556 = itertools.product('JKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHI', repeat=7)
res55557 = itertools.product('KLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJ', repeat=7)
res55558 = itertools.product('LMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJK', repeat=7)
res55559 = itertools.product('MNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKL', repeat=7)
res66660 = itertools.product('NOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLM', repeat=7)
res66661 = itertools.product('OPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN', repeat=7)
res66662 = itertools.product('PQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNO', repeat=7)
res66663 = itertools.product('QRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP', repeat=7)
res66664 = itertools.product('RSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQ', repeat=7)
res66665 = itertools.product('STUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR', repeat=7)
res66666 = itertools.product('TUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRS', repeat=7)
res66667 = itertools.product('UVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRST', repeat=7)
res66668 = itertools.product('VWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTU', repeat=7)
res66669 = itertools.product('WXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV', repeat=7)
res77770 = itertools.product('XYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW', repeat=7)
res77771 = itertools.product('YZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWX', repeat=7)
res77772 = itertools.product('ZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXY', repeat=7)

res222222 = itertools.product('bcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZa', repeat=8)
res222223 = itertools.product('cdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZab', repeat=8)
res222224 = itertools.product('defghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabc', repeat=8)
res222225 = itertools.product('efghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcd', repeat=8)
res222226 = itertools.product('fghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcde', repeat=8)
res222227 = itertools.product('ghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdef', repeat=8)
res222228 = itertools.product('hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefg', repeat=8)
res222229 = itertools.product('ijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefgh', repeat=8)
res333330 = itertools.product('jklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgi', repeat=8)
res333331 = itertools.product('klmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgij', repeat=8)
res333332 = itertools.product('lmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijk', repeat=8)
res333333 = itertools.product('mnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijkl', repeat=8)
res333334 = itertools.product('nopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklm', repeat=8)
res333335 = itertools.product('opqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmn', repeat=8)
res333336 = itertools.product('pqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmno', repeat=8)
res333337 = itertools.product('qrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnop', repeat=8)
res333338 = itertools.product('rstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnop1', repeat=8)
res333339 = itertools.product('stuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqr', repeat=8)
res444440 = itertools.product('tuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrs', repeat=8)
res444441 = itertools.product('uvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrst', repeat=8)
res444442 = itertools.product('vwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstu', repeat=8)
res444443 = itertools.product('wxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuv', repeat=8)
res444444 = itertools.product('xyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvw', repeat=8)
res444445 = itertools.product('yzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwx', repeat=8)
res444446 = itertools.product('zABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxy', repeat=8)
res444447 = itertools.product('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyz', repeat=8)
res444448 = itertools.product('BCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzA', repeat=8)
res444449 = itertools.product('CDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzAB', repeat=8)
res555550 = itertools.product('DEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABC', repeat=8)
res555551 = itertools.product('EFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCD', repeat=8)
res555552 = itertools.product('FGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDE', repeat=8)
res555553 = itertools.product('GHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEF', repeat=8)
res555554 = itertools.product('HIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFG', repeat=8)
res555555 = itertools.product('IJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGH', repeat=8)
res555556 = itertools.product('JKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHI', repeat=8)
res555557 = itertools.product('KLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJ', repeat=8)
res555558 = itertools.product('LMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJK', repeat=8)
res555559 = itertools.product('MNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKL', repeat=8)
res666660 = itertools.product('NOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLM', repeat=8)
res666661 = itertools.product('OPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN', repeat=8)
res666662 = itertools.product('PQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNO', repeat=8)
res666663 = itertools.product('QRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP', repeat=8)
res666664 = itertools.product('RSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQ', repeat=8)
res666665 = itertools.product('STUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR', repeat=8)
res666666 = itertools.product('TUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRS', repeat=8)
res666667 = itertools.product('UVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRST', repeat=8)
res666668 = itertools.product('VWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTU', repeat=8)
res666669 = itertools.product('WXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV', repeat=8)
res777770 = itertools.product('XYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW', repeat=8)
res777771 = itertools.product('YZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWX', repeat=8)
res777772 = itertools.product('ZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXY', repeat=8)

res2222222 = itertools.product('bcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZa', repeat=9)
res2222223 = itertools.product('cdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZab', repeat=9)
res2222224 = itertools.product('defghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabc', repeat=9)
res2222225 = itertools.product('efghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcd', repeat=9)
res2222226 = itertools.product('fghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcde', repeat=9)
res2222227 = itertools.product('ghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdef', repeat=9)
res2222228 = itertools.product('hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefg', repeat=9)
res2222229 = itertools.product('ijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefgh', repeat=9)
res3333330 = itertools.product('jklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgi', repeat=9)
res3333331 = itertools.product('klmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgij', repeat=9)
res3333332 = itertools.product('lmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijk', repeat=9)
res3333333 = itertools.product('mnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijkl', repeat=9)
res3333334 = itertools.product('nopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklm', repeat=9)
res3333335 = itertools.product('opqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmn', repeat=9)
res3333336 = itertools.product('pqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmno', repeat=9)
res3333337 = itertools.product('qrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnop', repeat=9)
res3333338 = itertools.product('rstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnop1', repeat=9)
res3333339 = itertools.product('stuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqr', repeat=9)
res4444440 = itertools.product('tuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrs', repeat=9)
res4444441 = itertools.product('uvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrst', repeat=9)
res4444442 = itertools.product('vwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstu', repeat=9)
res4444443 = itertools.product('wxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuv', repeat=9)
res4444444 = itertools.product('xyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvw', repeat=9)
res4444445 = itertools.product('yzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwx', repeat=9)
res4444446 = itertools.product('zABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxy', repeat=9)
res4444447 = itertools.product('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyz', repeat=9)
res4444448 = itertools.product('BCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzA', repeat=9)
res4444449 = itertools.product('CDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzAB', repeat=9)
res5555550 = itertools.product('DEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABC', repeat=9)
res5555551 = itertools.product('EFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCD', repeat=9)
res5555552 = itertools.product('FGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDE', repeat=9)
res5555553 = itertools.product('GHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEF', repeat=9)
res5555554 = itertools.product('HIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFG', repeat=9)
res5555555 = itertools.product('IJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGH', repeat=9)
res5555556 = itertools.product('JKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHI', repeat=9)
res5555557 = itertools.product('KLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJ', repeat=9)
res5555558 = itertools.product('LMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJK', repeat=9)
res5555559 = itertools.product('MNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKL', repeat=9)
res6666660 = itertools.product('NOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLM', repeat=9)
res6666661 = itertools.product('OPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN', repeat=9)
res6666662 = itertools.product('PQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNO', repeat=9)
res6666663 = itertools.product('QRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP', repeat=9)
res6666664 = itertools.product('RSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQ', repeat=9)
res6666665 = itertools.product('STUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR', repeat=9)
res6666666 = itertools.product('TUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRS', repeat=9)
res6666667 = itertools.product('UVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRST', repeat=9)
res6666668 = itertools.product('VWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTU', repeat=9)
res6666669 = itertools.product('WXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV', repeat=9)
res7777770 = itertools.product('XYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW', repeat=9)
res7777771 = itertools.product('YZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWX', repeat=9)
res7777772 = itertools.product('ZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXY', repeat=9)

res22222222 = itertools.product('bcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZa', repeat=10)
res22222223 = itertools.product('cdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZab', repeat=10)
res22222224 = itertools.product('defghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabc', repeat=10)
res22222225 = itertools.product('efghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcd', repeat=10)
res22222226 = itertools.product('fghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcde', repeat=10)
res22222227 = itertools.product('ghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdef', repeat=10)
res22222228 = itertools.product('hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefg', repeat=10)
res22222229 = itertools.product('ijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefgh', repeat=10)
res33333330 = itertools.product('jklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgi', repeat=10)
res33333331 = itertools.product('klmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgij', repeat=10)
res33333332 = itertools.product('lmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijk', repeat=10)
res33333333 = itertools.product('mnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijkl', repeat=10)
res33333334 = itertools.product('nopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklm', repeat=10)
res33333335 = itertools.product('opqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmn', repeat=10)
res33333336 = itertools.product('pqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmno', repeat=10)
res33333337 = itertools.product('qrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnop', repeat=10)
res33333338 = itertools.product('rstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnop1', repeat=10)
res33333339 = itertools.product('stuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqr', repeat=10)
res44444440 = itertools.product('tuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrs', repeat=10)
res44444441 = itertools.product('uvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrst', repeat=10)
res44444442 = itertools.product('vwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstu', repeat=10)
res44444443 = itertools.product('wxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuv', repeat=10)
res44444444 = itertools.product('xyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvw', repeat=10)
res44444445 = itertools.product('yzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwx', repeat=10)
res44444446 = itertools.product('zABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxy', repeat=10)
res44444447 = itertools.product('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyz', repeat=10)
res44444448 = itertools.product('BCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzA', repeat=10)
res44444449 = itertools.product('CDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzAB', repeat=10)
res55555550 = itertools.product('DEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABC', repeat=10)
res55555551 = itertools.product('EFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCD', repeat=10)
res55555552 = itertools.product('FGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDE', repeat=10)
res55555553 = itertools.product('GHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEF', repeat=10)
res55555554 = itertools.product('HIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFG', repeat=10)
res55555555 = itertools.product('IJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGH', repeat=10)
res55555556 = itertools.product('JKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHI', repeat=10)
res55555557 = itertools.product('KLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJ', repeat=10)
res55555558 = itertools.product('LMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJK', repeat=10)
res55555559 = itertools.product('MNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKL', repeat=10)
res66666660 = itertools.product('NOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLM', repeat=10)
res66666661 = itertools.product('OPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN', repeat=10)
res66666662 = itertools.product('PQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNO', repeat=10)
res66666663 = itertools.product('QRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP', repeat=10)
res66666664 = itertools.product('RSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQ', repeat=10)
res66666665 = itertools.product('STUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR', repeat=10)
res66666666 = itertools.product('TUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRS', repeat=10)
res66666667 = itertools.product('UVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRST', repeat=10)
res66666668 = itertools.product('VWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTU', repeat=10)
res66666669 = itertools.product('WXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV', repeat=10)
res77777770 = itertools.product('XYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW', repeat=10)
res77777771 = itertools.product('YZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWX', repeat=10)

res222222222 = itertools.product('bcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZa', repeat=11)
res222222223 = itertools.product('cdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZab', repeat=11)
res222222224 = itertools.product('defghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabc', repeat=11)
res222222225 = itertools.product('efghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcd', repeat=11)
res222222226 = itertools.product('fghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcde', repeat=11)
res222222227 = itertools.product('ghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdef', repeat=11)
res222222228 = itertools.product('hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefg', repeat=11)
res222222229 = itertools.product('ijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefgh', repeat=11)
res333333330 = itertools.product('jklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgi', repeat=11)
res333333331 = itertools.product('klmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgij', repeat=11)
res333333332 = itertools.product('lmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijk', repeat=11)
res333333333 = itertools.product('mnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijkl', repeat=11)
res333333334 = itertools.product('nopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklm', repeat=11)
res333333335 = itertools.product('opqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmn', repeat=11)
res333333336 = itertools.product('pqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmno', repeat=11)
res333333337 = itertools.product('qrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnop', repeat=11)
res333333338 = itertools.product('rstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnop1', repeat=11)
res333333339 = itertools.product('stuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqr', repeat=11)
res444444440 = itertools.product('tuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrs', repeat=11)
res444444441 = itertools.product('uvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrst', repeat=11)
res444444442 = itertools.product('vwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstu', repeat=11)
res444444443 = itertools.product('wxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuv', repeat=11)
res444444444 = itertools.product('xyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvw', repeat=11)
res444444445 = itertools.product('yzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwx', repeat=11)
res444444446 = itertools.product('zABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxy', repeat=11)
res444444447 = itertools.product('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyz', repeat=11)
res444444448 = itertools.product('BCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzA', repeat=11)
res444444449 = itertools.product('CDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzAB', repeat=11)
res555555550 = itertools.product('DEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABC', repeat=11)
res555555551 = itertools.product('EFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCD', repeat=11)
res555555552 = itertools.product('FGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDE', repeat=11)
res555555553 = itertools.product('GHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEF', repeat=11)
res555555554 = itertools.product('HIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFG', repeat=11)
res555555555 = itertools.product('IJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGH', repeat=11)
res555555556 = itertools.product('JKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHI', repeat=11)
res555555557 = itertools.product('KLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJ', repeat=11)
res555555558 = itertools.product('LMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJK', repeat=11)
res555555559 = itertools.product('MNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKL', repeat=11)
res666666660 = itertools.product('NOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLM', repeat=11)
res666666661 = itertools.product('OPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN', repeat=11)
res666666662 = itertools.product('PQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNO', repeat=11)
res666666663 = itertools.product('QRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP', repeat=11)
res666666664 = itertools.product('RSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQ', repeat=11)
res666666665 = itertools.product('STUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR', repeat=11)
res666666666 = itertools.product('TUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRS', repeat=11)
res666666667 = itertools.product('UVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRST', repeat=11)
res666666668 = itertools.product('VWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTU', repeat=11)
res666666669 = itertools.product('WXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV', repeat=11)
res777777770 = itertools.product('XYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW', repeat=11)
res777777771 = itertools.product('YZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWX', repeat=11)

res2222222222 = itertools.product('bcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZa', repeat=12)
res2222222223 = itertools.product('cdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZab', repeat=12)
res2222222224 = itertools.product('defghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabc', repeat=12)
res2222222225 = itertools.product('efghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcd', repeat=12)
res2222222226 = itertools.product('fghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcde', repeat=12)
res2222222227 = itertools.product('ghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdef', repeat=12)
res2222222228 = itertools.product('hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefg', repeat=12)
res2222222229 = itertools.product('ijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefgh', repeat=12)
res3333333330 = itertools.product('jklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgi', repeat=12)
res3333333331 = itertools.product('klmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgij', repeat=12)
res3333333332 = itertools.product('lmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijk', repeat=12)
res3333333333 = itertools.product('mnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijkl', repeat=12)
res3333333334 = itertools.product('nopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklm', repeat=12)
res3333333335 = itertools.product('opqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmn', repeat=12)
res3333333336 = itertools.product('pqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmno', repeat=12)
res3333333337 = itertools.product('qrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnop', repeat=12)
res3333333338 = itertools.product('rstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnop1', repeat=12)
res3333333339 = itertools.product('stuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqr', repeat=12)
res4444444440 = itertools.product('tuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrs', repeat=12)
res4444444441 = itertools.product('uvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrst', repeat=12)
res4444444442 = itertools.product('vwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstu', repeat=12)
res4444444443 = itertools.product('wxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuv', repeat=12)
res4444444444 = itertools.product('xyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvw', repeat=12)
res4444444445 = itertools.product('yzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwx', repeat=12)
res4444444446 = itertools.product('zABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxy', repeat=12)
res4444444447 = itertools.product('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyz', repeat=12)
res4444444448 = itertools.product('BCDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzA', repeat=12)
res4444444449 = itertools.product('CDEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzAB', repeat=12)
res5555555550 = itertools.product('DEFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABC', repeat=12)
res5555555551 = itertools.product('EFGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCD', repeat=12)
res5555555552 = itertools.product('FGHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDE', repeat=12)
res5555555553 = itertools.product('GHIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEF', repeat=12)
res5555555554 = itertools.product('HIJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFG', repeat=12)
res5555555555 = itertools.product('IJKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGH', repeat=12)
res5555555556 = itertools.product('JKLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHI', repeat=12)
res5555555557 = itertools.product('KLMNOPQRSTUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJ', repeat=12)
res5555555558 = itertools.product('LMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJK', repeat=12)
res5555555559 = itertools.product('MNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKL', repeat=12)
res6666666660 = itertools.product('NOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLM', repeat=12)
res6666666661 = itertools.product('OPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN', repeat=12)
res6666666662 = itertools.product('PQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNO', repeat=12)
res6666666663 = itertools.product('QRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP', repeat=12)
res6666666664 = itertools.product('RSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQ', repeat=12)
res6666666665 = itertools.product('STUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR', repeat=12)
res6666666666 = itertools.product('TUVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRS', repeat=12)
res6666666667 = itertools.product('UVWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRST', repeat=12)
res6666666668 = itertools.product('VWXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTU', repeat=12)
res6666666669 = itertools.product('WXYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV', repeat=12)
res7777777770 = itertools.product('XYZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW', repeat=12)
res7777777771 = itertools.product('YZabcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWX', repeat=12)

res4a1	= itertools.product('bcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|a', repeat=4)
res4a2	= itertools.product('cdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|bc', repeat=4)
res4a3	= itertools.product('defghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abc', repeat=4)
res4a4	= itertools.product('efghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcd', repeat=4)
res4a5	= itertools.product('fghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcde', repeat=4)
res4a6	= itertools.product('ghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdef', repeat=4)
res4a7	= itertools.product('hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefg', repeat=4)
res4a8	= itertools.product('ijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefgh', repeat=4)
res4a9	= itertools.product('jklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghi', repeat=4)
res4a10	= itertools.product('klmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghij', repeat=4)
res4a11	= itertools.product('lmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijk', repeat=4)
res4a12	= itertools.product('mnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijkl', repeat=4)
res4a13	= itertools.product('nopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklm', repeat=4)
res4a14	= itertools.product('opqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmn', repeat=4)
res4a15	= itertools.product('pqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmno', repeat=4)
res4a16	= itertools.product('qrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnop', repeat=4)
res4a17	= itertools.product('rstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopq', repeat=4)
res4a18	= itertools.product('stuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqr', repeat=4)
res4a19	= itertools.product('tuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrs', repeat=4)
res4a20	= itertools.product('uvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrst', repeat=4)
res4a21	= itertools.product('vwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstu', repeat=4)
res4a22	= itertools.product('xyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvw', repeat=4)
res4a23	= itertools.product('yzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwx', repeat=4)
res4a24	= itertools.product('zABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxy', repeat=4)
res4a25	= itertools.product('ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyz', repeat=4)
res4a26	= itertools.product('BCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzA', repeat=4)
res4a27	= itertools.product('CDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzAB', repeat=4)
res4a28	= itertools.product('DEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABC', repeat=4)
res4a29	= itertools.product('EFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCD', repeat=4)
res4a30	= itertools.product('FGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDE', repeat=4)
res4a31	= itertools.product('GHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEF', repeat=4)
res4a32	= itertools.product('HIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFG', repeat=4)
res4a33	= itertools.product('IJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGH', repeat=4)
res4a34	= itertools.product('JKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHI', repeat=4)
res4a35	= itertools.product('KLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJ', repeat=4)
res4a36	= itertools.product('LMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJK', repeat=4)
res4a37	= itertools.product('MNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKL', repeat=4)
res4a38	= itertools.product('NOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLM', repeat=4)
res4a39	= itertools.product('OPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN', repeat=4)
res4a40	= itertools.product('PQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNO', repeat=4)
res4a41	= itertools.product('QRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP', repeat=4)
res4a42	= itertools.product('RSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQ', repeat=4)
res4a43	= itertools.product('STUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR', repeat=4)
res4a44	= itertools.product('TUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRS', repeat=4)
res4a45	= itertools.product('UVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRST', repeat=4)
res4a46	= itertools.product('VWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTU', repeat=4)
res4a47	= itertools.product('WXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV', repeat=4)
res4a48	= itertools.product('XYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW', repeat=4)
res4a49	= itertools.product('YZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWX', repeat=4)
res4a50	= itertools.product('Z123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXY', repeat=4)
res4a51	= itertools.product('123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=4)
res4a52	= itertools.product('23456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1', repeat=4)
res4a53	= itertools.product('3456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12', repeat=4)
res4a54	= itertools.product('456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123', repeat=4)
res4a55	= itertools.product('56789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234', repeat=4)
res4a56	= itertools.product('6789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345', repeat=4)
res4a57	= itertools.product('789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456', repeat=4)
res4a58	= itertools.product('89!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567', repeat=4)
res4a59	= itertools.product('9!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345678', repeat=4)
res4a60	= itertools.product('!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789', repeat=4)
res4a61	= itertools.product('@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!', repeat=4)
res4a62	= itertools.product('#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@', repeat=4)
res4a63	= itertools.product('$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#', repeat=4)
res4a64	= itertools.product('%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$', repeat=4)
res4a65	= itertools.product('^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%', repeat=4)
res4a66	= itertools.product('&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^', repeat=4)
res4a67	= itertools.product('*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&', repeat=4)
res4a68	= itertools.product('()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*', repeat=4)
res4a69	= itertools.product(')_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*(', repeat=4)
res4a70	= itertools.product('_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()', repeat=4)
res4a71	= itertools.product('+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()+', repeat=4)
res4a72	= itertools.product(',./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+', repeat=4)
res4a73	= itertools.product('./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,', repeat=4)
res4a74	= itertools.product('/;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,.', repeat=4)
res4a75	= itertools.product(';"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./', repeat=4)
res4a76	= itertools.product('"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;', repeat=4)
res4a77	= itertools.product('{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"', repeat=4)
res4a78	= itertools.product('}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{', repeat=4)
res4a79	= itertools.product('|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}', repeat=4)
res4b1	= itertools.product('bcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|a', repeat=5)
res4b2	= itertools.product('cdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|bc', repeat=5)
res4b3	= itertools.product('defghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abc', repeat=5)
res4b4	= itertools.product('efghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcd', repeat=5)
res4b5	= itertools.product('fghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcde', repeat=5)
res4b6	= itertools.product('ghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdef', repeat=5)
res4b7	= itertools.product('hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefg', repeat=5)
res4b8	= itertools.product('ijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefgh', repeat=5)
res4b9	= itertools.product('jklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghi', repeat=5)
res4b10	= itertools.product('klmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghij', repeat=5)
res4b11	= itertools.product('lmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijk', repeat=5)
res4b12	= itertools.product('mnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijkl', repeat=5)
res4b13	= itertools.product('nopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklm', repeat=5)
res4b14	= itertools.product('opqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmn', repeat=5)
res4b15	= itertools.product('pqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmno', repeat=5)
res4b16	= itertools.product('qrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnop', repeat=5)
res4b17	= itertools.product('rstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopq', repeat=5)
res4b18	= itertools.product('stuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqr', repeat=5)
res4b19	= itertools.product('tuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrs', repeat=5)
res4b20	= itertools.product('uvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrst', repeat=5)
res4b21	= itertools.product('vwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstu', repeat=5)
res4b22	= itertools.product('xyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvw', repeat=5)
res4b23	= itertools.product('yzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwx', repeat=5)
res4b24	= itertools.product('zABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxy', repeat=5)
res4b25	= itertools.product('ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyz', repeat=5)
res4b26	= itertools.product('BCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzA', repeat=5)
res4b27	= itertools.product('CDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzAB', repeat=5)
res4b28	= itertools.product('DEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABC', repeat=5)
res4b29	= itertools.product('EFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCD', repeat=5)
res4b30	= itertools.product('FGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDE', repeat=5)
res4b31	= itertools.product('GHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEF', repeat=5)
res4b32	= itertools.product('HIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFG', repeat=5)
res4b33	= itertools.product('IJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGH', repeat=5)
res4b34	= itertools.product('JKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHI', repeat=5)
res4b35	= itertools.product('KLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJ', repeat=5)
res4b36	= itertools.product('LMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJK', repeat=5)
res4b37	= itertools.product('MNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKL', repeat=5)
res4b38	= itertools.product('NOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLM', repeat=5)
res4b39	= itertools.product('OPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN', repeat=5)
res4b40	= itertools.product('PQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNO', repeat=5)
res4b41	= itertools.product('QRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP', repeat=5)
res4b42	= itertools.product('RSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQ', repeat=5)
res4b43	= itertools.product('STUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR', repeat=5)
res4b44	= itertools.product('TUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRS', repeat=5)
res4b45	= itertools.product('UVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRST', repeat=5)
res4b46	= itertools.product('VWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTU', repeat=5)
res4b47	= itertools.product('WXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV', repeat=5)
res4b48	= itertools.product('XYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW', repeat=5)
res4b49	= itertools.product('YZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWX', repeat=5)
res4b50	= itertools.product('Z123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXY', repeat=5)
res4b51	= itertools.product('123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=5)
res4b52	= itertools.product('23456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1', repeat=5)
res4b53	= itertools.product('3456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12', repeat=5)
res4b54	= itertools.product('456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123', repeat=5)
res4b55	= itertools.product('56789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234', repeat=5)
res4b56	= itertools.product('6789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345', repeat=5)
res4b57	= itertools.product('789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456', repeat=5)
res4b58	= itertools.product('89!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567', repeat=5)
res4b59	= itertools.product('9!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345678', repeat=5)
res4b60	= itertools.product('!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789', repeat=5)
res4b61	= itertools.product('@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!', repeat=5)
res4b62	= itertools.product('#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@', repeat=5)
res4b63	= itertools.product('$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#', repeat=5)
res4b64	= itertools.product('%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$', repeat=5)
res4b65	= itertools.product('^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%', repeat=5)
res4b66	= itertools.product('&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^', repeat=5)
res4b67	= itertools.product('*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&', repeat=5)
res4b68	= itertools.product('()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*', repeat=5)
res4b69	= itertools.product(')_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*(', repeat=5)
res4b70	= itertools.product('_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()', repeat=5)
res4b71	= itertools.product('+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()+', repeat=5)
res4b72	= itertools.product(',./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+', repeat=5)
res4b73	= itertools.product('./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,', repeat=5)
res4b74	= itertools.product('/;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,.', repeat=5)
res4b75	= itertools.product(';"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./', repeat=5)
res4b76	= itertools.product('"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;', repeat=5)
res4b77	= itertools.product('{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"', repeat=5)
res4b78	= itertools.product('}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{', repeat=5)
res4b79	= itertools.product('|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}', repeat=5)
res4c1	= itertools.product('bcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|a', repeat=6)
res4c2	= itertools.product('cdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|bc', repeat=6)
res4c3	= itertools.product('defghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abc', repeat=6)
res4c4	= itertools.product('efghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcd', repeat=6)
res4c5	= itertools.product('fghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcde', repeat=6)
res4c6	= itertools.product('ghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdef', repeat=6)
res4c7	= itertools.product('hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefg', repeat=6)
res4c8	= itertools.product('ijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefgh', repeat=6)
res4c9	= itertools.product('jklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghi', repeat=6)
res4c10	= itertools.product('klmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghij', repeat=6)
res4c11	= itertools.product('lmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijk', repeat=6)
res4c12	= itertools.product('mnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijkl', repeat=6)
res4c13	= itertools.product('nopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklm', repeat=6)
res4c14	= itertools.product('opqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmn', repeat=6)
res4c15	= itertools.product('pqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmno', repeat=6)
res4c16	= itertools.product('qrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnop', repeat=6)
res4c17	= itertools.product('rstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopq', repeat=6)
res4c18	= itertools.product('stuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqr', repeat=6)
res4c19	= itertools.product('tuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrs', repeat=6)
res4c20	= itertools.product('uvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrst', repeat=6)
res4c21	= itertools.product('vwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstu', repeat=6)
res4c22	= itertools.product('xyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvw', repeat=6)
res4c23	= itertools.product('yzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwx', repeat=6)
res4c24	= itertools.product('zABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxy', repeat=6)
res4c25	= itertools.product('ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyz', repeat=6)
res4c26	= itertools.product('BCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzA', repeat=6)
res4c27	= itertools.product('CDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzAB', repeat=6)
res4c28	= itertools.product('DEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABC', repeat=6)
res4c29	= itertools.product('EFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCD', repeat=6)
res4c30	= itertools.product('FGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDE', repeat=6)
res4c31	= itertools.product('GHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEF', repeat=6)
res4c32	= itertools.product('HIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFG', repeat=6)
res4c33	= itertools.product('IJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGH', repeat=6)
res4c34	= itertools.product('JKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHI', repeat=6)
res4c35	= itertools.product('KLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJ', repeat=6)
res4c36	= itertools.product('LMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJK', repeat=6)
res4c37	= itertools.product('MNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKL', repeat=6)
res4c38	= itertools.product('NOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLM', repeat=6)
res4c39	= itertools.product('OPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN', repeat=6)
res4c40	= itertools.product('PQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNO', repeat=6)
res4c41	= itertools.product('QRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP', repeat=6)
res4c42	= itertools.product('RSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQ', repeat=6)
res4c43	= itertools.product('STUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR', repeat=6)
res4c44	= itertools.product('TUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRS', repeat=6)
res4c45	= itertools.product('UVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRST', repeat=6)
res4c46	= itertools.product('VWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTU', repeat=6)
res4c47	= itertools.product('WXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV', repeat=6)
res4c48	= itertools.product('XYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW', repeat=6)
res4c49	= itertools.product('YZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWX', repeat=6)
res4c50	= itertools.product('Z123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXY', repeat=6)
res4c51	= itertools.product('123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=6)
res4c52	= itertools.product('23456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1', repeat=6)
res4c53	= itertools.product('3456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12', repeat=6)
res4c54	= itertools.product('456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123', repeat=6)
res4c55	= itertools.product('56789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234', repeat=6)
res4c56	= itertools.product('6789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345', repeat=6)
res4c57	= itertools.product('789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456', repeat=6)
res4c58	= itertools.product('89!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567', repeat=6)
res4c59	= itertools.product('9!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345678', repeat=6)
res4c60	= itertools.product('!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789', repeat=6)
res4c61	= itertools.product('@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!', repeat=6)
res4c62	= itertools.product('#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@', repeat=6)
res4c63	= itertools.product('$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#', repeat=6)
res4c64	= itertools.product('%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$', repeat=6)
res4c65	= itertools.product('^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%', repeat=6)
res4c66	= itertools.product('&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^', repeat=6)
res4c67	= itertools.product('*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&', repeat=6)
res4c68	= itertools.product('()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*', repeat=6)
res4c69	= itertools.product(')_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*(', repeat=6)
res4c70	= itertools.product('_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()', repeat=6)
res4c71	= itertools.product('+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()+', repeat=6)
res4c72	= itertools.product(',./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+', repeat=6)
res4c73	= itertools.product('./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,', repeat=6)
res4c74	= itertools.product('/;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,.', repeat=6)
res4c75	= itertools.product(';"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./', repeat=6)
res4c76	= itertools.product('"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;', repeat=6)
res4c77	= itertools.product('{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"', repeat=6)
res4c78	= itertools.product('}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{', repeat=6)
res4c79	= itertools.product('|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}', repeat=6)
res4d1	= itertools.product('bcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|a', repeat=7)
res4d2	= itertools.product('cdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|bc', repeat=7)
res4d3	= itertools.product('defghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abc', repeat=7)
res4d4	= itertools.product('efghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcd', repeat=7)
res4d5	= itertools.product('fghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcde', repeat=7)
res4d6	= itertools.product('ghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdef', repeat=7)
res4d7	= itertools.product('hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefg', repeat=7)
res4d8	= itertools.product('ijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefgh', repeat=7)
res4d9	= itertools.product('jklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghi', repeat=7)
res4d10	= itertools.product('klmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghij', repeat=7)
res4d11	= itertools.product('lmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijk', repeat=7)
res4d12	= itertools.product('mnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijkl', repeat=7)
res4d13	= itertools.product('nopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklm', repeat=7)
res4d14	= itertools.product('opqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmn', repeat=7)
res4d15	= itertools.product('pqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmno', repeat=7)
res4d16	= itertools.product('qrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnop', repeat=7)
res4d17	= itertools.product('rstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopq', repeat=7)
res4d18	= itertools.product('stuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqr', repeat=7)
res4d19	= itertools.product('tuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrs', repeat=7)
res4d20	= itertools.product('uvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrst', repeat=7)
res4d21	= itertools.product('vwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstu', repeat=7)
res4d22	= itertools.product('xyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvw', repeat=7)
res4d23	= itertools.product('yzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwx', repeat=7)
res4d24	= itertools.product('zABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxy', repeat=7)
res4d25	= itertools.product('ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyz', repeat=7)
res4d26	= itertools.product('BCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzA', repeat=7)
res4d27	= itertools.product('CDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzAB', repeat=7)
res4d28	= itertools.product('DEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABC', repeat=7)
res4d29	= itertools.product('EFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCD', repeat=7)
res4d30	= itertools.product('FGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDE', repeat=7)
res4d31	= itertools.product('GHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEF', repeat=7)
res4d32	= itertools.product('HIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFG', repeat=7)
res4d33	= itertools.product('IJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGH', repeat=7)
res4d34	= itertools.product('JKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHI', repeat=7)
res4d35	= itertools.product('KLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJ', repeat=7)
res4d36	= itertools.product('LMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJK', repeat=7)
res4d37	= itertools.product('MNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKL', repeat=7)
res4d38	= itertools.product('NOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLM', repeat=7)
res4d39	= itertools.product('OPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN', repeat=7)
res4d40	= itertools.product('PQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNO', repeat=7)
res4d41	= itertools.product('QRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP', repeat=7)
res4d42	= itertools.product('RSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQ', repeat=7)
res4d43	= itertools.product('STUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR', repeat=7)
res4d44	= itertools.product('TUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRS', repeat=7)
res4d45	= itertools.product('UVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRST', repeat=7)
res4d46	= itertools.product('VWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTU', repeat=7)
res4d47	= itertools.product('WXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV', repeat=7)
res4d48	= itertools.product('XYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW', repeat=7)
res4d49	= itertools.product('YZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWX', repeat=7)
res4d50	= itertools.product('Z123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXY', repeat=7)
res4d51	= itertools.product('123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=7)
res4d52	= itertools.product('23456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1', repeat=7)
res4d53	= itertools.product('3456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12', repeat=7)
res4d54	= itertools.product('456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123', repeat=7)
res4d55	= itertools.product('56789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234', repeat=7)
res4d56	= itertools.product('6789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345', repeat=7)
res4d57	= itertools.product('789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456', repeat=7)
res4d58	= itertools.product('89!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567', repeat=7)
res4d59	= itertools.product('9!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345678', repeat=7)
res4d60	= itertools.product('!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789', repeat=7)
res4d61	= itertools.product('@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!', repeat=7)
res4d62	= itertools.product('#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@', repeat=7)
res4d63	= itertools.product('$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#', repeat=7)
res4d64	= itertools.product('%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$', repeat=7)
res4d65	= itertools.product('^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%', repeat=7)
res4d66	= itertools.product('&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^', repeat=7)
res4d67	= itertools.product('*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&', repeat=7)
res4d68	= itertools.product('()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*', repeat=7)
res4d69	= itertools.product(')_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*(', repeat=7)
res4d70	= itertools.product('_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()', repeat=7)
res4d71	= itertools.product('+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()+', repeat=7)
res4d72	= itertools.product(',./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+', repeat=7)
res4d73	= itertools.product('./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,', repeat=7)
res4d74	= itertools.product('/;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,.', repeat=7)
res4d75	= itertools.product(';"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./', repeat=7)
res4d76	= itertools.product('"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;', repeat=7)
res4d77	= itertools.product('{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"', repeat=7)
res4d78	= itertools.product('}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{', repeat=7)
res4d79	= itertools.product('|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}', repeat=7)
res4e1	= itertools.product('bcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|a', repeat=8)
res4e2	= itertools.product('cdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|bc', repeat=8)
res4e3	= itertools.product('defghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abc', repeat=8)
res4e4	= itertools.product('efghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcd', repeat=8)
res4e5	= itertools.product('fghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcde', repeat=8)
res4e6	= itertools.product('ghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdef', repeat=8)
res4e7	= itertools.product('hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefg', repeat=8)
res4e8	= itertools.product('ijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefgh', repeat=8)
res4e9	= itertools.product('jklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghi', repeat=8)
res4e10	= itertools.product('klmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghij', repeat=8)
res4e11	= itertools.product('lmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijk', repeat=8)
res4e12	= itertools.product('mnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijkl', repeat=8)
res4e13	= itertools.product('nopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklm', repeat=8)
res4e14	= itertools.product('opqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmn', repeat=8)
res4e15	= itertools.product('pqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmno', repeat=8)
res4e16	= itertools.product('qrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnop', repeat=8)
res4e17	= itertools.product('rstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopq', repeat=8)
res4e18	= itertools.product('stuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqr', repeat=8)
res4e19	= itertools.product('tuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrs', repeat=8)
res4e20	= itertools.product('uvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrst', repeat=8)
res4e21	= itertools.product('vwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstu', repeat=8)
res4e22	= itertools.product('xyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvw', repeat=8)
res4e23	= itertools.product('yzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwx', repeat=8)
res4e24	= itertools.product('zABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxy', repeat=8)
res4e25	= itertools.product('ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyz', repeat=8)
res4e26	= itertools.product('BCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzA', repeat=8)
res4e27	= itertools.product('CDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzAB', repeat=8)
res4e28	= itertools.product('DEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABC', repeat=8)
res4e29	= itertools.product('EFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCD', repeat=8)
res4e30	= itertools.product('FGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDE', repeat=8)
res4e31	= itertools.product('GHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEF', repeat=8)
res4e32	= itertools.product('HIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFG', repeat=8)
res4e33	= itertools.product('IJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGH', repeat=8)
res4e34	= itertools.product('JKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHI', repeat=8)
res4e35	= itertools.product('KLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJ', repeat=8)
res4e36	= itertools.product('LMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJK', repeat=8)
res4e37	= itertools.product('MNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKL', repeat=8)
res4e38	= itertools.product('NOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLM', repeat=8)
res4e39	= itertools.product('OPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN', repeat=8)
res4e40	= itertools.product('PQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNO', repeat=8)
res4e41	= itertools.product('QRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP', repeat=8)
res4e42	= itertools.product('RSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQ', repeat=8)
res4e43	= itertools.product('STUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR', repeat=8)
res4e44	= itertools.product('TUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRS', repeat=8)
res4e45	= itertools.product('UVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRST', repeat=8)
res4e46	= itertools.product('VWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTU', repeat=8)
res4e47	= itertools.product('WXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV', repeat=8)
res4e48	= itertools.product('XYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW', repeat=8)
res4e49	= itertools.product('YZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWX', repeat=8)
res4e50	= itertools.product('Z123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXY', repeat=8)
res4e51	= itertools.product('123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=8)
res4e52	= itertools.product('23456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1', repeat=8)
res4e53	= itertools.product('3456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12', repeat=8)
res4e54	= itertools.product('456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123', repeat=8)
res4e55	= itertools.product('56789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234', repeat=8)
res4e56	= itertools.product('6789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345', repeat=8)
res4e57	= itertools.product('789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456', repeat=8)
res4e58	= itertools.product('89!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567', repeat=8)
res4e59	= itertools.product('9!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345678', repeat=8)
res4e60	= itertools.product('!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789', repeat=8)
res4e61	= itertools.product('@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!', repeat=8)
res4e62	= itertools.product('#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@', repeat=8)
res4e63	= itertools.product('$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#', repeat=8)
res4e64	= itertools.product('%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$', repeat=8)
res4e65	= itertools.product('^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%', repeat=8)
res4e66	= itertools.product('&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^', repeat=8)
res4e67	= itertools.product('*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&', repeat=8)
res4e68	= itertools.product('()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*', repeat=8)
res4e69	= itertools.product(')_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*(', repeat=8)
res4e70	= itertools.product('_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()', repeat=8)
res4e71	= itertools.product('+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()+', repeat=8)
res4e72	= itertools.product(',./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+', repeat=8)
res4e73	= itertools.product('./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,', repeat=8)
res4e74	= itertools.product('/;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,.', repeat=8)
res4e75	= itertools.product(';"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./', repeat=8)
res4e76	= itertools.product('"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;', repeat=8)
res4e77	= itertools.product('{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"', repeat=8)
res4e78	= itertools.product('}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{', repeat=8)
res4e79	= itertools.product('|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}', repeat=8)
res4f1	= itertools.product('bcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|a', repeat=9)
res4f2	= itertools.product('cdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|bc', repeat=9)
res4f3	= itertools.product('defghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abc', repeat=9)
res4f4	= itertools.product('efghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcd', repeat=9)
res4f5	= itertools.product('fghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcde', repeat=9)
res4f6	= itertools.product('ghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdef', repeat=9)
res4f7	= itertools.product('hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefg', repeat=9)
res4f8	= itertools.product('ijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefgh', repeat=9)
res4f9	= itertools.product('jklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghi', repeat=9)
res4f10	= itertools.product('klmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghij', repeat=9)
res4f11	= itertools.product('lmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijk', repeat=9)
res4f12	= itertools.product('mnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijkl', repeat=9)
res4f13	= itertools.product('nopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklm', repeat=9)
res4f14	= itertools.product('opqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmn', repeat=9)
res4f15	= itertools.product('pqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmno', repeat=9)
res4f16	= itertools.product('qrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnop', repeat=9)
res4f17	= itertools.product('rstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopq', repeat=9)
res4f18	= itertools.product('stuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqr', repeat=9)
res4f19	= itertools.product('tuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrs', repeat=9)
res4f20	= itertools.product('uvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrst', repeat=9)
res4f21	= itertools.product('vwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstu', repeat=9)
res4f22	= itertools.product('xyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvw', repeat=9)
res4f23	= itertools.product('yzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwx', repeat=9)
res4f24	= itertools.product('zABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxy', repeat=9)
res4f25	= itertools.product('ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyz', repeat=9)
res4f26	= itertools.product('BCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzA', repeat=9)
res4f27	= itertools.product('CDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzAB', repeat=9)
res4f28	= itertools.product('DEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABC', repeat=9)
res4f29	= itertools.product('EFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCD', repeat=9)
res4f30	= itertools.product('FGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDE', repeat=9)
res4f31	= itertools.product('GHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEF', repeat=9)
res4f32	= itertools.product('HIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFG', repeat=9)
res4f33	= itertools.product('IJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGH', repeat=9)
res4f34	= itertools.product('JKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHI', repeat=9)
res4f35	= itertools.product('KLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJ', repeat=9)
res4f36	= itertools.product('LMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJK', repeat=9)
res4f37	= itertools.product('MNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKL', repeat=9)
res4f38	= itertools.product('NOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLM', repeat=9)
res4f39	= itertools.product('OPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN', repeat=9)
res4f40	= itertools.product('PQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNO', repeat=9)
res4f41	= itertools.product('QRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP', repeat=9)
res4f42	= itertools.product('RSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQ', repeat=9)
res4f43	= itertools.product('STUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR', repeat=9)
res4f44	= itertools.product('TUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRS', repeat=9)
res4f45	= itertools.product('UVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRST', repeat=9)
res4f46	= itertools.product('VWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTU', repeat=9)
res4f47	= itertools.product('WXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV', repeat=9)
res4f48	= itertools.product('XYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW', repeat=9)
res4f49	= itertools.product('YZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWX', repeat=9)
res4f50	= itertools.product('Z123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXY', repeat=9)
res4f51	= itertools.product('123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=9)
res4f52	= itertools.product('23456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1', repeat=9)
res4f53	= itertools.product('3456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12', repeat=9)
res4f54	= itertools.product('456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123', repeat=9)
res4f55	= itertools.product('56789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234', repeat=9)
res4f56	= itertools.product('6789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345', repeat=9)
res4f57	= itertools.product('789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456', repeat=9)
res4f58	= itertools.product('89!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567', repeat=9)
res4f59	= itertools.product('9!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345678', repeat=9)
res4f60	= itertools.product('!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789', repeat=9)
res4f61	= itertools.product('@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!', repeat=9)
res4f62	= itertools.product('#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@', repeat=9)
res4f63	= itertools.product('$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#', repeat=9)
res4f64	= itertools.product('%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$', repeat=9)
res4f65	= itertools.product('^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%', repeat=9)
res4f66	= itertools.product('&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^', repeat=9)
res4f67	= itertools.product('*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&', repeat=9)
res4f68	= itertools.product('()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*', repeat=9)
res4f69	= itertools.product(')_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*(', repeat=9)
res4f70	= itertools.product('_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()', repeat=9)
res4f71	= itertools.product('+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()+', repeat=9)
res4f72	= itertools.product(',./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+', repeat=9)
res4f73	= itertools.product('./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,', repeat=9)
res4f74	= itertools.product('/;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,.', repeat=9)
res4f75	= itertools.product(';"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./', repeat=9)
res4f76	= itertools.product('"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;', repeat=9)
res4f77	= itertools.product('{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"', repeat=9)
res4f78	= itertools.product('}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{', repeat=9)
res4f79	= itertools.product('|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}', repeat=9)
res4g1	= itertools.product('bcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|a', repeat=10)
res4g2	= itertools.product('cdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|bc', repeat=10)
res4g3	= itertools.product('defghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abc', repeat=10)
res4g4	= itertools.product('efghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcd', repeat=10)
res4g5	= itertools.product('fghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcde', repeat=10)
res4g6	= itertools.product('ghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdef', repeat=10)
res4g7	= itertools.product('hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefg', repeat=10)
res4g8	= itertools.product('ijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefgh', repeat=10)
res4g9	= itertools.product('jklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghi', repeat=10)
res4g10	= itertools.product('klmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghij', repeat=10)
res4g11	= itertools.product('lmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijk', repeat=10)
res4g12	= itertools.product('mnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijkl', repeat=10)
res4g13	= itertools.product('nopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklm', repeat=10)
res4g14	= itertools.product('opqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmn', repeat=10)
res4g15	= itertools.product('pqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmno', repeat=10)
res4g16	= itertools.product('qrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnop', repeat=10)
res4g17	= itertools.product('rstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopq', repeat=10)
res4g18	= itertools.product('stuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqr', repeat=10)
res4g19	= itertools.product('tuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrs', repeat=10)
res4g20	= itertools.product('uvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrst', repeat=10)
res4g21	= itertools.product('vwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstu', repeat=10)
res4g22	= itertools.product('xyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvw', repeat=10)
res4g23	= itertools.product('yzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwx', repeat=10)
res4g24	= itertools.product('zABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxy', repeat=10)
res4g25	= itertools.product('ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyz', repeat=10)
res4g26	= itertools.product('BCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzA', repeat=10)
res4g27	= itertools.product('CDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzAB', repeat=10)
res4g28	= itertools.product('DEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABC', repeat=10)
res4g29	= itertools.product('EFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCD', repeat=10)
res4g30	= itertools.product('FGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDE', repeat=10)
res4g31	= itertools.product('GHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEF', repeat=10)
res4g32	= itertools.product('HIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFG', repeat=10)
res4g33	= itertools.product('IJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGH', repeat=10)
res4g34	= itertools.product('JKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHI', repeat=10)
res4g35	= itertools.product('KLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJ', repeat=10)
res4g36	= itertools.product('LMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJK', repeat=10)
res4g37	= itertools.product('MNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKL', repeat=10)
res4g38	= itertools.product('NOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLM', repeat=10)
res4g39	= itertools.product('OPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN', repeat=10)
res4g40	= itertools.product('PQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNO', repeat=10)
res4g41	= itertools.product('QRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP', repeat=10)
res4g42	= itertools.product('RSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQ', repeat=10)
res4g43	= itertools.product('STUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR', repeat=10)
res4g44	= itertools.product('TUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRS', repeat=10)
res4g45	= itertools.product('UVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRST', repeat=10)
res4g46	= itertools.product('VWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTU', repeat=10)
res4g47	= itertools.product('WXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV', repeat=10)
res4g48	= itertools.product('XYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW', repeat=10)
res4g49	= itertools.product('YZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWX', repeat=10)
res4g50	= itertools.product('Z123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXY', repeat=10)
res4g51	= itertools.product('123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=10)
res4g52	= itertools.product('23456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1', repeat=10)
res4g53	= itertools.product('3456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12', repeat=10)
res4g54	= itertools.product('456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123', repeat=10)
res4g55	= itertools.product('56789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234', repeat=10)
res4g56	= itertools.product('6789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345', repeat=10)
res4g57	= itertools.product('789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456', repeat=10)
res4g58	= itertools.product('89!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567', repeat=10)
res4g59	= itertools.product('9!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345678', repeat=10)
res4g60	= itertools.product('!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789', repeat=10)
res4g61	= itertools.product('@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!', repeat=10)
res4g62	= itertools.product('#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@', repeat=10)
res4g63	= itertools.product('$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#', repeat=10)
res4g64	= itertools.product('%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$', repeat=10)
res4g65	= itertools.product('^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%', repeat=10)
res4g66	= itertools.product('&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^', repeat=10)
res4g67	= itertools.product('*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&', repeat=10)
res4g68	= itertools.product('()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*', repeat=10)
res4g69	= itertools.product(')_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*(', repeat=10)
res4g70	= itertools.product('_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()', repeat=10)
res4g71	= itertools.product('+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()+', repeat=10)
res4g72	= itertools.product(',./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+', repeat=10)
res4g73	= itertools.product('./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,', repeat=10)
res4g74	= itertools.product('/;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,.', repeat=10)
res4g75	= itertools.product(';"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./', repeat=10)
res4g76	= itertools.product('"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;', repeat=10)
res4g77	= itertools.product('{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"', repeat=10)
res4g78	= itertools.product('}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{', repeat=10)
res4g79	= itertools.product('|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}', repeat=10)
res4h1	= itertools.product('bcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|a', repeat=11)
res4h2	= itertools.product('cdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|bc', repeat=11)
res4h3	= itertools.product('defghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abc', repeat=11)
res4h4	= itertools.product('efghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcd', repeat=11)
res4h5	= itertools.product('fghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcde', repeat=11)
res4h6	= itertools.product('ghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdef', repeat=11)
res4h7	= itertools.product('hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefg', repeat=11)
res4h8	= itertools.product('ijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefgh', repeat=11)
res4h9	= itertools.product('jklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghi', repeat=11)
res4h10	= itertools.product('klmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghij', repeat=11)
res4h11	= itertools.product('lmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijk', repeat=11)
res4h12	= itertools.product('mnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijkl', repeat=11)
res4h13	= itertools.product('nopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklm', repeat=11)
res4h14	= itertools.product('opqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmn', repeat=11)
res4h15	= itertools.product('pqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmno', repeat=11)
res4h16	= itertools.product('qrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnop', repeat=11)
res4h17	= itertools.product('rstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopq', repeat=11)
res4h18	= itertools.product('stuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqr', repeat=11)
res4h19	= itertools.product('tuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrs', repeat=11)
res4h20	= itertools.product('uvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrst', repeat=11)
res4h21	= itertools.product('vwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstu', repeat=11)
res4h22	= itertools.product('xyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvw', repeat=11)
res4h23	= itertools.product('yzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwx', repeat=11)
res4h24	= itertools.product('zABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxy', repeat=11)
res4h25	= itertools.product('ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyz', repeat=11)
res4h26	= itertools.product('BCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzA', repeat=11)
res4h27	= itertools.product('CDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzAB', repeat=11)
res4h28	= itertools.product('DEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABC', repeat=11)
res4h29	= itertools.product('EFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCD', repeat=11)
res4h30	= itertools.product('FGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDE', repeat=11)
res4h31	= itertools.product('GHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEF', repeat=11)
res4h32	= itertools.product('HIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFG', repeat=11)
res4h33	= itertools.product('IJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGH', repeat=11)
res4h34	= itertools.product('JKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHI', repeat=11)
res4h35	= itertools.product('KLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJ', repeat=11)
res4h36	= itertools.product('LMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJK', repeat=11)
res4h37	= itertools.product('MNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKL', repeat=11)
res4h38	= itertools.product('NOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLM', repeat=11)
res4h39	= itertools.product('OPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN', repeat=11)
res4h40	= itertools.product('PQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNO', repeat=11)
res4h41	= itertools.product('QRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP', repeat=11)
res4h42	= itertools.product('RSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQ', repeat=11)
res4h43	= itertools.product('STUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR', repeat=11)
res4h44	= itertools.product('TUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRS', repeat=11)
res4h45	= itertools.product('UVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRST', repeat=11)
res4h46	= itertools.product('VWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTU', repeat=11)
res4h47	= itertools.product('WXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV', repeat=11)
res4h48	= itertools.product('XYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW', repeat=11)
res4h49	= itertools.product('YZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWX', repeat=11)
res4h50	= itertools.product('Z123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXY', repeat=11)
res4h51	= itertools.product('123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=11)
res4h52	= itertools.product('23456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1', repeat=11)
res4h53	= itertools.product('3456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12', repeat=11)
res4h54	= itertools.product('456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123', repeat=11)
res4h55	= itertools.product('56789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234', repeat=11)
res4h56	= itertools.product('6789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345', repeat=11)
res4h57	= itertools.product('789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456', repeat=11)
res4h58	= itertools.product('89!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567', repeat=11)
res4h59	= itertools.product('9!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345678', repeat=11)
res4h60	= itertools.product('!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789', repeat=11)
res4h61	= itertools.product('@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!', repeat=11)
res4h62	= itertools.product('#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@', repeat=11)
res4h63	= itertools.product('$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#', repeat=11)
res4h64	= itertools.product('%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$', repeat=11)
res4h65	= itertools.product('^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%', repeat=11)
res4h66	= itertools.product('&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^', repeat=11)
res4h67	= itertools.product('*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&', repeat=11)
res4h68	= itertools.product('()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*', repeat=11)
res4h69	= itertools.product(')_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*(', repeat=11)
res4h70	= itertools.product('_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()', repeat=11)
res4h71	= itertools.product('+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()+', repeat=11)
res4h72	= itertools.product(',./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+', repeat=11)
res4h73	= itertools.product('./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,', repeat=11)
res4h74	= itertools.product('/;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,.', repeat=11)
res4h75	= itertools.product(';"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./', repeat=11)
res4h76	= itertools.product('"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;', repeat=11)
res4h77	= itertools.product('{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"', repeat=11)
res4h78	= itertools.product('}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{', repeat=11)
res4h79	= itertools.product('|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}', repeat=11)
res4i1	= itertools.product('bcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|a', repeat=12)
res4i2	= itertools.product('cdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|bc', repeat=12)
res4i3	= itertools.product('defghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abc', repeat=12)
res4i4	= itertools.product('efghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcd', repeat=12)
res4i5	= itertools.product('fghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcde', repeat=12)
res4i6	= itertools.product('ghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdef', repeat=12)
res4i7	= itertools.product('hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefg', repeat=12)
res4i8	= itertools.product('ijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefgh', repeat=12)
res4i9	= itertools.product('jklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghi', repeat=12)
res4i10	= itertools.product('klmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghij', repeat=12)
res4i11	= itertools.product('lmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijk', repeat=12)
res4i12	= itertools.product('mnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijkl', repeat=12)
res4i13	= itertools.product('nopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklm', repeat=12)
res4i14	= itertools.product('opqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmn', repeat=12)
res4i15	= itertools.product('pqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmno', repeat=12)
res4i16	= itertools.product('qrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnop', repeat=12)
res4i17	= itertools.product('rstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopq', repeat=12)
res4i18	= itertools.product('stuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqr', repeat=12)
res4i19	= itertools.product('tuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrs', repeat=12)
res4i20	= itertools.product('uvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrst', repeat=12)
res4i21	= itertools.product('vwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstu', repeat=12)
res4i22	= itertools.product('xyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvw', repeat=12)
res4i23	= itertools.product('yzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwx', repeat=12)
res4i24	= itertools.product('zABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxy', repeat=12)
res4i25	= itertools.product('ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyz', repeat=12)
res4i26	= itertools.product('BCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzA', repeat=12)
res4i27	= itertools.product('CDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzAB', repeat=12)
res4i28	= itertools.product('DEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABC', repeat=12)
res4i29	= itertools.product('EFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCD', repeat=12)
res4i30	= itertools.product('FGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDE', repeat=12)
res4i31	= itertools.product('GHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEF', repeat=12)
res4i32	= itertools.product('HIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFG', repeat=12)
res4i33	= itertools.product('IJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGH', repeat=12)
res4i34	= itertools.product('JKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHI', repeat=12)
res4i35	= itertools.product('KLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJ', repeat=12)
res4i36	= itertools.product('LMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJK', repeat=12)
res4i37	= itertools.product('MNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKL', repeat=12)
res4i38	= itertools.product('NOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLM', repeat=12)
res4i39	= itertools.product('OPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN', repeat=12)
res4i40	= itertools.product('PQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNO', repeat=12)
res4i41	= itertools.product('QRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP', repeat=12)
res4i42	= itertools.product('RSTUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQ', repeat=12)
res4i43	= itertools.product('STUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR', repeat=12)
res4i44	= itertools.product('TUVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRS', repeat=12)
res4i45	= itertools.product('UVWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRST', repeat=12)
res4i46	= itertools.product('VWXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTU', repeat=12)
res4i47	= itertools.product('WXYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV', repeat=12)
res4i48	= itertools.product('XYZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW', repeat=12)
res4i49	= itertools.product('YZ123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWX', repeat=12)
res4i50	= itertools.product('Z123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXY', repeat=12)
res4i51	= itertools.product('123456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=12)
res4i52	= itertools.product('23456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1', repeat=12)
res4i53	= itertools.product('3456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12', repeat=12)
res4i54	= itertools.product('456789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123', repeat=12)
res4i55	= itertools.product('56789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234', repeat=12)
res4i56	= itertools.product('6789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345', repeat=12)
res4i57	= itertools.product('789!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456', repeat=12)
res4i58	= itertools.product('89!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567', repeat=12)
res4i59	= itertools.product('9!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345678', repeat=12)
res4i60	= itertools.product('!@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789', repeat=12)
res4i61	= itertools.product('@#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!', repeat=12)
res4i62	= itertools.product('#$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@', repeat=12)
res4i63	= itertools.product('$%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#', repeat=12)
res4i64	= itertools.product('%^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$', repeat=12)
res4i65	= itertools.product('^&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%', repeat=12)
res4i66	= itertools.product('&*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^', repeat=12)
res4i67	= itertools.product('*()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&', repeat=12)
res4i68	= itertools.product('()_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*', repeat=12)
res4i69	= itertools.product(')_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*(', repeat=12)
res4i70	= itertools.product('_+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()', repeat=12)
res4i71	= itertools.product('+,./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()+', repeat=12)
res4i72	= itertools.product(',./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+', repeat=12)
res4i73	= itertools.product('./;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,', repeat=12)
res4i74	= itertools.product('/;"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,.', repeat=12)
res4i75	= itertools.product(';"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./', repeat=12)
res4i76	= itertools.product('"{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;', repeat=12)
res4i77	= itertools.product('{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"', repeat=12)
res4i78	= itertools.product('}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{', repeat=12)
res4i79	= itertools.product('|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+,./;"{}', repeat=12)

def gen4a10():
    for i in res4a10: 
        print ''.join(i)
def gen4a11():
    for i in res4a11: 
        print ''.join(i)
def gen4a12():
    for i in res4a12: 
        print ''.join(i)
def gen4a13():
    for i in res4a13: 
        print ''.join(i)
def gen4a14():
    for i in res4a14: 
        print ''.join(i)
def gen4a15():
    for i in res4a15: 
        print ''.join(i)
def gen4a16():
    for i in res4a16: 
        print ''.join(i)
def gen4a17():
    for i in res4a17: 
        print ''.join(i)
def gen4a18():
    for i in res4a18: 
        print ''.join(i)
def gen4a19():
    for i in res4a19: 
        print ''.join(i)
def gen4a1():
    for i in res4a1: 
        print ''.join(i)
def gen4a20():
    for i in res4a20: 
        print ''.join(i)
def gen4a21():
    for i in res4a21: 
        print ''.join(i)
def gen4a22():
    for i in res4a22: 
        print ''.join(i)
def gen4a23():
    for i in res4a23: 
        print ''.join(i)
def gen4a24():
    for i in res4a24: 
        print ''.join(i)
def gen4a25():
    for i in res4a25: 
        print ''.join(i)
def gen4a26():
    for i in res4a26: 
        print ''.join(i)
def gen4a27():
    for i in res4a27: 
        print ''.join(i)
def gen4a28():
    for i in res4a28: 
        print ''.join(i)
def gen4a29():
    for i in res4a29: 
        print ''.join(i)
def gen4a2():
    for i in res4a2: 
        print ''.join(i)
def gen4a30():
    for i in res4a30: 
        print ''.join(i)
def gen4a31():
    for i in res4a31: 
        print ''.join(i)
def gen4a32():
    for i in res4a32: 
        print ''.join(i)
def gen4a33():
    for i in res4a33: 
        print ''.join(i)
def gen4a34():
    for i in res4a34: 
        print ''.join(i)
def gen4a35():
    for i in res4a35: 
        print ''.join(i)
def gen4a36():
    for i in res4a36: 
        print ''.join(i)
def gen4a37():
    for i in res4a37: 
        print ''.join(i)
def gen4a38():
    for i in res4a38: 
        print ''.join(i)
def gen4a39():
    for i in res4a39: 
        print ''.join(i)
def gen4a3():
    for i in res4a3: 
        print ''.join(i)
def gen4a40():
    for i in res4a40: 
        print ''.join(i)
def gen4a41():
    for i in res4a41: 
        print ''.join(i)
def gen4a42():
    for i in res4a42: 
        print ''.join(i)
def gen4a43():
    for i in res4a43: 
        print ''.join(i)
def gen4a44():
    for i in res4a44: 
        print ''.join(i)
def gen4a45():
    for i in res4a45: 
        print ''.join(i)
def gen4a46():
    for i in res4a46: 
        print ''.join(i)
def gen4a47():
    for i in res4a47: 
        print ''.join(i)
def gen4a48():
    for i in res4a48: 
        print ''.join(i)
def gen4a49():
    for i in res4a49: 
        print ''.join(i)
def gen4a4():
    for i in res4a4: 
        print ''.join(i)
def gen4a50():
    for i in res4a50: 
        print ''.join(i)
def gen4a51():
    for i in res4a51: 
        print ''.join(i)
def gen4a52():
    for i in res4a52: 
        print ''.join(i)
def gen4a53():
    for i in res4a53: 
        print ''.join(i)
def gen4a54():
    for i in res4a54: 
        print ''.join(i)
def gen4a55():
    for i in res4a55: 
        print ''.join(i)
def gen4a56():
    for i in res4a56: 
        print ''.join(i)
def gen4a57():
    for i in res4a57: 
        print ''.join(i)
def gen4a58():
    for i in res4a58: 
        print ''.join(i)
def gen4a59():
    for i in res4a59: 
        print ''.join(i)
def gen4a5():
    for i in res4a5: 
        print ''.join(i)
def gen4a60():
    for i in res4a60: 
        print ''.join(i)
def gen4a61():
    for i in res4a61: 
        print ''.join(i)
def gen4a62():
    for i in res4a62: 
        print ''.join(i)
def gen4a63():
    for i in res4a63: 
        print ''.join(i)
def gen4a64():
    for i in res4a64: 
        print ''.join(i)
def gen4a65():
    for i in res4a65: 
        print ''.join(i)
def gen4a66():
    for i in res4a66: 
        print ''.join(i)
def gen4a67():
    for i in res4a67: 
        print ''.join(i)
def gen4a68():
    for i in res4a68: 
        print ''.join(i)
def gen4a69():
    for i in res4a69: 
        print ''.join(i)
def gen4a6():
    for i in res4a6: 
        print ''.join(i)
def gen4a70():
    for i in res4a70: 
        print ''.join(i)
def gen4a71():
    for i in res4a71: 
        print ''.join(i)
def gen4a72():
    for i in res4a72: 
        print ''.join(i)
def gen4a73():
    for i in res4a73: 
        print ''.join(i)
def gen4a74():
    for i in res4a74: 
        print ''.join(i)
def gen4a75():
    for i in res4a75: 
        print ''.join(i)
def gen4a76():
    for i in res4a76: 
        print ''.join(i)
def gen4a77():
    for i in res4a77: 
        print ''.join(i)
def gen4a78():
    for i in res4a78: 
        print ''.join(i)
def gen4a79():
    for i in res4a79: 
        print ''.join(i)
def gen4a7():
    for i in res4a7: 
        print ''.join(i)
def gen4a8():
    for i in res4a8: 
        print ''.join(i)
def gen4a9():
    for i in res4a9: 
        print ''.join(i)
def gen4():
    for i in res4: 
        print ''.join(i)
def gen5():
    for i in res5: 
        print ''.join(i)
def gen6():
    for i in res6: 
        print ''.join(i)
def gen7():
    for i in res7: 
        print ''.join(i)
def gen8():
    for i in res8: 
        print ''.join(i)
def gen9():
    for i in res9: 
        print ''.join(i)
def gen10():
    for i in res10: 
        print ''.join(i)
def gen11():
    for i in res11: 
        print ''.join(i)
def gen12():
    for i in res12: 
        print ''.join(i)
def gen13():
    for i in res13: 
        print ''.join(i)
def gen14():
    for i in res14: 
        print ''.join(i)
def gen15():
    for i in res15: 
        print ''.join(i)
def gen16():
    for i in res16: 
        print ''.join(i)
def gen17():
    for i in res17: 
        print ''.join(i)
def gen18():
    for i in res18: 
        print ''.join(i)
def gen19():
    for i in res19: 
        print ''.join(i)
def gen20():
    for i in res20: 
        print ''.join(i)
def gen21():
    for i in res21: 
        print ''.join(i)
def gen4b10():
    for i in res4b10: 
        print ''.join(i)
def gen4b11():
    for i in res4b11: 
        print ''.join(i)
def gen4b12():
    for i in res4b12: 
        print ''.join(i)
def gen4b13():
    for i in res4b13: 
        print ''.join(i)
def gen4b14():
    for i in res4b14: 
        print ''.join(i)
def gen4b15():
    for i in res4b15: 
        print ''.join(i)
def gen4b16():
    for i in res4b16: 
        print ''.join(i)
def gen4b17():
    for i in res4b17: 
        print ''.join(i)
def gen4b18():
    for i in res4b18: 
        print ''.join(i)
def gen4b19():
    for i in res4b19: 
        print ''.join(i)
def gen4b1():
    for i in res4b1: 
        print ''.join(i)
def gen4b20():
    for i in res4b20: 
        print ''.join(i)
def gen4b21():
    for i in res4b21: 
        print ''.join(i)
def gen4b22():
    for i in res4b22: 
        print ''.join(i)
def gen4b23():
    for i in res4b23: 
        print ''.join(i)
def gen4b24():
    for i in res4b24: 
        print ''.join(i)
def gen4b25():
    for i in res4b25: 
        print ''.join(i)
def gen4b26():
    for i in res4b26: 
        print ''.join(i)
def gen4b27():
    for i in res4b27: 
        print ''.join(i)
def gen4b28():
    for i in res4b28: 
        print ''.join(i)
def gen4b29():
    for i in res4b29: 
        print ''.join(i)
def gen4b2():
    for i in res4b2: 
        print ''.join(i)
def gen4b30():
    for i in res4b30: 
        print ''.join(i)
def gen4b31():
    for i in res4b31: 
        print ''.join(i)
def gen4b32():
    for i in res4b32: 
        print ''.join(i)
def gen4b33():
    for i in res4b33: 
        print ''.join(i)
def gen4b34():
    for i in res4b34: 
        print ''.join(i)
def gen4b35():
    for i in res4b35: 
        print ''.join(i)
def gen4b36():
    for i in res4b36: 
        print ''.join(i)
def gen4b37():
    for i in res4b37: 
        print ''.join(i)
def gen4b38():
    for i in res4b38: 
        print ''.join(i)
def gen4b39():
    for i in res4b39: 
        print ''.join(i)
def gen4b3():
    for i in res4b3: 
        print ''.join(i)
def gen4b40():
    for i in res4b40: 
        print ''.join(i)
def gen4b41():
    for i in res4b41: 
        print ''.join(i)
def gen4b42():
    for i in res4b42: 
        print ''.join(i)
def gen4b43():
    for i in res4b43: 
        print ''.join(i)
def gen4b44():
    for i in res4b44: 
        print ''.join(i)
def gen4b45():
    for i in res4b45: 
        print ''.join(i)
def gen4b46():
    for i in res4b46: 
        print ''.join(i)
def gen4b47():
    for i in res4b47: 
        print ''.join(i)
def gen4b48():
    for i in res4b48: 
        print ''.join(i)
def gen4b49():
    for i in res4b49: 
        print ''.join(i)
def gen4b4():
    for i in res4b4: 
        print ''.join(i)
def gen4b50():
    for i in res4b50: 
        print ''.join(i)
def gen4b51():
    for i in res4b51: 
        print ''.join(i)
def gen4b52():
    for i in res4b52: 
        print ''.join(i)
def gen4b53():
    for i in res4b53: 
        print ''.join(i)
def gen4b54():
    for i in res4b54: 
        print ''.join(i)
def gen4b55():
    for i in res4b55: 
        print ''.join(i)
def gen4b56():
    for i in res4b56: 
        print ''.join(i)
def gen4b57():
    for i in res4b57: 
        print ''.join(i)
def gen4b58():
    for i in res4b58: 
        print ''.join(i)
def gen4b59():
    for i in res4b59: 
        print ''.join(i)
def gen4b5():
    for i in res4b5: 
        print ''.join(i)
def gen4b60():
    for i in res4b60: 
        print ''.join(i)
def gen4b61():
    for i in res4b61: 
        print ''.join(i)
def gen4b62():
    for i in res4b62: 
        print ''.join(i)
def gen4b63():
    for i in res4b63: 
        print ''.join(i)
def gen4b64():
    for i in res4b64: 
        print ''.join(i)
def gen4b65():
    for i in res4b65: 
        print ''.join(i)
def gen4b66():
    for i in res4b66: 
        print ''.join(i)
def gen4b67():
    for i in res4b67: 
        print ''.join(i)
def gen4b68():
    for i in res4b68: 
        print ''.join(i)
def gen4b69():
    for i in res4b69: 
        print ''.join(i)
def gen4b6():
    for i in res4b6: 
        print ''.join(i)
def gen4b70():
    for i in res4b70: 
        print ''.join(i)
def gen4b71():
    for i in res4b71: 
        print ''.join(i)
def gen4b72():
    for i in res4b72: 
        print ''.join(i)
def gen4b73():
    for i in res4b73: 
        print ''.join(i)
def gen4b74():
    for i in res4b74: 
        print ''.join(i)
def gen4b75():
    for i in res4b75: 
        print ''.join(i)
def gen4b76():
    for i in res4b76: 
        print ''.join(i)
def gen4b77():
    for i in res4b77: 
        print ''.join(i)
def gen4b78():
    for i in res4b78: 
        print ''.join(i)
def gen4b79():
    for i in res4b79: 
        print ''.join(i)
def gen4b7():
    for i in res4b7: 
        print ''.join(i)
def gen4b8():
    for i in res4b8: 
        print ''.join(i)
def gen4b9():
    for i in res4b9: 
        print ''.join(i)
def gen4c10():
    for i in res4c10: 
        print ''.join(i)
def gen4c11():
    for i in res4c11: 
        print ''.join(i)
def gen4c12():
    for i in res4c12: 
        print ''.join(i)
def gen4c13():
    for i in res4c13: 
        print ''.join(i)
def gen4c14():
    for i in res4c14: 
        print ''.join(i)
def gen4c15():
    for i in res4c15: 
        print ''.join(i)
def gen4c16():
    for i in res4c16: 
        print ''.join(i)
def gen4c17():
    for i in res4c17: 
        print ''.join(i)
def gen4c18():
    for i in res4c18: 
        print ''.join(i)
def gen4c19():
    for i in res4c19: 
        print ''.join(i)
def gen4c1():
    for i in res4c1: 
        print ''.join(i)
def gen4c20():
    for i in res4c20: 
        print ''.join(i)
def gen4c21():
    for i in res4c21: 
        print ''.join(i)
def gen4c22():
    for i in res4c22: 
        print ''.join(i)
def gen4c23():
    for i in res4c23: 
        print ''.join(i)
def gen4c24():
    for i in res4c24: 
        print ''.join(i)
def gen4c25():
    for i in res4c25: 
        print ''.join(i)
def gen4c26():
    for i in res4c26: 
        print ''.join(i)
def gen4c27():
    for i in res4c27: 
        print ''.join(i)
def gen4c28():
    for i in res4c28: 
        print ''.join(i)
def gen4c29():
    for i in res4c29: 
        print ''.join(i)
def gen4c2():
    for i in res4c2: 
        print ''.join(i)
def gen4c30():
    for i in res4c30: 
        print ''.join(i)
def gen4c31():
    for i in res4c31: 
        print ''.join(i)
def gen4c32():
    for i in res4c32: 
        print ''.join(i)
def gen4c33():
    for i in res4c33: 
        print ''.join(i)
def gen4c34():
    for i in res4c34: 
        print ''.join(i)
def gen4c35():
    for i in res4c35: 
        print ''.join(i)
def gen4c36():
    for i in res4c36: 
        print ''.join(i)
def gen4c37():
    for i in res4c37: 
        print ''.join(i)
def gen4c38():
    for i in res4c38: 
        print ''.join(i)
def gen4c39():
    for i in res4c39: 
        print ''.join(i)
def gen4c3():
    for i in res4c3: 
        print ''.join(i)
def gen4c40():
    for i in res4c40: 
        print ''.join(i)
def gen4c41():
    for i in res4c41: 
        print ''.join(i)
def gen4c42():
    for i in res4c42: 
        print ''.join(i)
def gen4c43():
    for i in res4c43: 
        print ''.join(i)
def gen4c44():
    for i in res4c44: 
        print ''.join(i)
def gen4c45():
    for i in res4c45: 
        print ''.join(i)
def gen4c46():
    for i in res4c46: 
        print ''.join(i)
def gen4c47():
    for i in res4c47: 
        print ''.join(i)
def gen4c48():
    for i in res4c48: 
        print ''.join(i)
def gen4c49():
    for i in res4c49: 
        print ''.join(i)
def gen4c4():
    for i in res4c4: 
        print ''.join(i)
def gen4c50():
    for i in res4c50: 
        print ''.join(i)
def gen4c51():
    for i in res4c51: 
        print ''.join(i)
def gen4c52():
    for i in res4c52: 
        print ''.join(i)
def gen4c53():
    for i in res4c53: 
        print ''.join(i)
def gen4c54():
    for i in res4c54: 
        print ''.join(i)
def gen4c55():
    for i in res4c55: 
        print ''.join(i)
def gen4c56():
    for i in res4c56: 
        print ''.join(i)
def gen4c57():
    for i in res4c57: 
        print ''.join(i)
def gen4c58():
    for i in res4c58: 
        print ''.join(i)
def gen4c59():
    for i in res4c59: 
        print ''.join(i)
def gen4c5():
    for i in res4c5: 
        print ''.join(i)
def gen4c60():
    for i in res4c60: 
        print ''.join(i)
def gen4c61():
    for i in res4c61: 
        print ''.join(i)
def gen4c62():
    for i in res4c62: 
        print ''.join(i)
def gen4c63():
    for i in res4c63: 
        print ''.join(i)
def gen4c64():
    for i in res4c64: 
        print ''.join(i)
def gen4c65():
    for i in res4c65: 
        print ''.join(i)
def gen4c66():
    for i in res4c66: 
        print ''.join(i)
def gen4c67():
    for i in res4c67: 
        print ''.join(i)
def gen4c68():
    for i in res4c68: 
        print ''.join(i)
def gen4c69():
    for i in res4c69: 
        print ''.join(i)
def gen4c6():
    for i in res4c6: 
        print ''.join(i)
def gen4c70():
    for i in res4c70: 
        print ''.join(i)
def gen4c71():
    for i in res4c71: 
        print ''.join(i)
def gen4c72():
    for i in res4c72: 
        print ''.join(i)
def gen4c73():
    for i in res4c73: 
        print ''.join(i)
def gen4c74():
    for i in res4c74: 
        print ''.join(i)
def gen4c75():
    for i in res4c75: 
        print ''.join(i)
def gen4c76():
    for i in res4c76: 
        print ''.join(i)
def gen4c77():
    for i in res4c77: 
        print ''.join(i)
def gen4c78():
    for i in res4c78: 
        print ''.join(i)
def gen4c79():
    for i in res4c79: 
        print ''.join(i)
def gen4c7():
    for i in res4c7: 
        print ''.join(i)
def gen4c8():
    for i in res4c8: 
        print ''.join(i)
def gen4c9():
    for i in res4c9: 
        print ''.join(i)
def gen4d10():
    for i in res4d10: 
        print ''.join(i)
def gen4d11():
    for i in res4d11: 
        print ''.join(i)
def gen4d12():
    for i in res4d12: 
        print ''.join(i)
def gen4d13():
    for i in res4d13: 
        print ''.join(i)
def gen4d14():
    for i in res4d14: 
        print ''.join(i)
def gen4d15():
    for i in res4d15: 
        print ''.join(i)
def gen4d16():
    for i in res4d16: 
        print ''.join(i)
def gen4d17():
    for i in res4d17: 
        print ''.join(i)
def gen4d18():
    for i in res4d18: 
        print ''.join(i)
def gen4d19():
    for i in res4d19: 
        print ''.join(i)
def gen4d1():
    for i in res4d1: 
        print ''.join(i)
def gen4d20():
    for i in res4d20: 
        print ''.join(i)
def gen4d21():
    for i in res4d21: 
        print ''.join(i)
def gen4d22():
    for i in res4d22: 
        print ''.join(i)
def gen4d23():
    for i in res4d23: 
        print ''.join(i)
def gen4d24():
    for i in res4d24: 
        print ''.join(i)
def gen4d25():
    for i in res4d25: 
        print ''.join(i)
def gen4d26():
    for i in res4d26: 
        print ''.join(i)
def gen4d27():
    for i in res4d27: 
        print ''.join(i)
def gen4d28():
    for i in res4d28: 
        print ''.join(i)
def gen4d29():
    for i in res4d29: 
        print ''.join(i)
def gen4d2():
    for i in res4d2: 
        print ''.join(i)
def gen4d30():
    for i in res4d30: 
        print ''.join(i)
def gen4d31():
    for i in res4d31: 
        print ''.join(i)
def gen4d32():
    for i in res4d32: 
        print ''.join(i)
def gen4d33():
    for i in res4d33: 
        print ''.join(i)
def gen4d34():
    for i in res4d34: 
        print ''.join(i)
def gen4d35():
    for i in res4d35: 
        print ''.join(i)
def gen4d36():
    for i in res4d36: 
        print ''.join(i)
def gen4d37():
    for i in res4d37: 
        print ''.join(i)
def gen4d38():
    for i in res4d38: 
        print ''.join(i)
def gen4d39():
    for i in res4d39: 
        print ''.join(i)
def gen4d3():
    for i in res4d3: 
        print ''.join(i)
def gen4d40():
    for i in res4d40: 
        print ''.join(i)
def gen4d41():
    for i in res4d41: 
        print ''.join(i)
def gen4d42():
    for i in res4d42: 
        print ''.join(i)
def gen4d43():
    for i in res4d43: 
        print ''.join(i)
def gen4d44():
    for i in res4d44: 
        print ''.join(i)
def gen4d45():
    for i in res4d45: 
        print ''.join(i)
def gen4d46():
    for i in res4d46: 
        print ''.join(i)
def gen4d47():
    for i in res4d47: 
        print ''.join(i)
def gen4d48():
    for i in res4d48: 
        print ''.join(i)
def gen4d49():
    for i in res4d49: 
        print ''.join(i)
def gen4d4():
    for i in res4d4: 
        print ''.join(i)
def gen4d50():
    for i in res4d50: 
        print ''.join(i)
def gen4d51():
    for i in res4d51: 
        print ''.join(i)
def gen4d52():
    for i in res4d52: 
        print ''.join(i)
def gen4d53():
    for i in res4d53: 
        print ''.join(i)
def gen4d54():
    for i in res4d54: 
        print ''.join(i)
def gen4d55():
    for i in res4d55: 
        print ''.join(i)
def gen4d56():
    for i in res4d56: 
        print ''.join(i)
def gen4d57():
    for i in res4d57: 
        print ''.join(i)
def gen4d58():
    for i in res4d58: 
        print ''.join(i)
def gen4d59():
    for i in res4d59: 
        print ''.join(i)
def gen4d5():
    for i in res4d5: 
        print ''.join(i)
def gen4d60():
    for i in res4d60: 
        print ''.join(i)
def gen4d61():
    for i in res4d61: 
        print ''.join(i)
def gen4d62():
    for i in res4d62: 
        print ''.join(i)
def gen4d63():
    for i in res4d63: 
        print ''.join(i)
def gen4d64():
    for i in res4d64: 
        print ''.join(i)
def gen4d65():
    for i in res4d65: 
        print ''.join(i)
def gen4d66():
    for i in res4d66: 
        print ''.join(i)
def gen4d67():
    for i in res4d67: 
        print ''.join(i)
def gen4d68():
    for i in res4d68: 
        print ''.join(i)
def gen4d69():
    for i in res4d69: 
        print ''.join(i)
def gen4d6():
    for i in res4d6: 
        print ''.join(i)
def gen4d70():
    for i in res4d70: 
        print ''.join(i)
def gen4d71():
    for i in res4d71: 
        print ''.join(i)
def gen4d72():
    for i in res4d72: 
        print ''.join(i)
def gen4d73():
    for i in res4d73: 
        print ''.join(i)
def gen4d74():
    for i in res4d74: 
        print ''.join(i)
def gen4d75():
    for i in res4d75: 
        print ''.join(i)
def gen4d76():
    for i in res4d76: 
        print ''.join(i)
def gen4d77():
    for i in res4d77: 
        print ''.join(i)
def gen4d78():
    for i in res4d78: 
        print ''.join(i)
def gen4d79():
    for i in res4d79: 
        print ''.join(i)
def gen4d7():
    for i in res4d7: 
        print ''.join(i)
def gen4d8():
    for i in res4d8: 
        print ''.join(i)
def gen4d9():
    for i in res4d9: 
        print ''.join(i)
def gen4e10():
    for i in res4e10: 
        print ''.join(i)
def gen4e11():
    for i in res4e11: 
        print ''.join(i)
def gen4e12():
    for i in res4e12: 
        print ''.join(i)
def gen4e13():
    for i in res4e13: 
        print ''.join(i)
def gen4e14():
    for i in res4e14: 
        print ''.join(i)
def gen4e15():
    for i in res4e15: 
        print ''.join(i)
def gen4e16():
    for i in res4e16: 
        print ''.join(i)
def gen4e17():
    for i in res4e17: 
        print ''.join(i)
def gen4e18():
    for i in res4e18: 
        print ''.join(i)
def gen4e19():
    for i in res4e19: 
        print ''.join(i)
def gen4e1():
    for i in res4e1: 
        print ''.join(i)
def gen4e20():
    for i in res4e20: 
        print ''.join(i)
def gen4e21():
    for i in res4e21: 
        print ''.join(i)
def gen4e22():
    for i in res4e22: 
        print ''.join(i)
def gen4e23():
    for i in res4e23: 
        print ''.join(i)
def gen4e24():
    for i in res4e24: 
        print ''.join(i)
def gen4e25():
    for i in res4e25: 
        print ''.join(i)
def gen4e26():
    for i in res4e26: 
        print ''.join(i)
def gen4e27():
    for i in res4e27: 
        print ''.join(i)
def gen4e28():
    for i in res4e28: 
        print ''.join(i)
def gen4e29():
    for i in res4e29: 
        print ''.join(i)
def gen4e2():
    for i in res4e2: 
        print ''.join(i)
def gen4e30():
    for i in res4e30: 
        print ''.join(i)
def gen4e31():
    for i in res4e31: 
        print ''.join(i)
def gen4e32():
    for i in res4e32: 
        print ''.join(i)
def gen4e33():
    for i in res4e33: 
        print ''.join(i)
def gen4e34():
    for i in res4e34: 
        print ''.join(i)
def gen4e35():
    for i in res4e35: 
        print ''.join(i)
def gen4e36():
    for i in res4e36: 
        print ''.join(i)
def gen4e37():
    for i in res4e37: 
        print ''.join(i)
def gen4e38():
    for i in res4e38: 
        print ''.join(i)
def gen4e39():
    for i in res4e39: 
        print ''.join(i)
def gen4e3():
    for i in res4e3: 
        print ''.join(i)
def gen4e40():
    for i in res4e40: 
        print ''.join(i)
def gen4e41():
    for i in res4e41: 
        print ''.join(i)
def gen4e42():
    for i in res4e42: 
        print ''.join(i)
def gen4e43():
    for i in res4e43: 
        print ''.join(i)
def gen4e44():
    for i in res4e44: 
        print ''.join(i)
def gen4e45():
    for i in res4e45: 
        print ''.join(i)
def gen4e46():
    for i in res4e46: 
        print ''.join(i)
def gen4e47():
    for i in res4e47: 
        print ''.join(i)
def gen4e48():
    for i in res4e48: 
        print ''.join(i)
def gen4e49():
    for i in res4e49: 
        print ''.join(i)
def gen4e4():
    for i in res4e4: 
        print ''.join(i)
def gen4e50():
    for i in res4e50: 
        print ''.join(i)
def gen4e51():
    for i in res4e51: 
        print ''.join(i)
def gen4e52():
    for i in res4e52: 
        print ''.join(i)
def gen4e53():
    for i in res4e53: 
        print ''.join(i)
def gen4e54():
    for i in res4e54: 
        print ''.join(i)
def gen4e55():
    for i in res4e55: 
        print ''.join(i)
def gen4e56():
    for i in res4e56: 
        print ''.join(i)
def gen4e57():
    for i in res4e57: 
        print ''.join(i)
def gen4e58():
    for i in res4e58: 
        print ''.join(i)
def gen4e59():
    for i in res4e59: 
        print ''.join(i)
def gen4e5():
    for i in res4e5: 
        print ''.join(i)
def gen4e60():
    for i in res4e60: 
        print ''.join(i)
def gen4e61():
    for i in res4e61: 
        print ''.join(i)
def gen4e62():
    for i in res4e62: 
        print ''.join(i)
def gen4e63():
    for i in res4e63: 
        print ''.join(i)
def gen4e64():
    for i in res4e64: 
        print ''.join(i)
def gen4e65():
    for i in res4e65: 
        print ''.join(i)
def gen4e66():
    for i in res4e66: 
        print ''.join(i)
def gen4e67():
    for i in res4e67: 
        print ''.join(i)
def gen4e68():
    for i in res4e68: 
        print ''.join(i)
def gen4e69():
    for i in res4e69: 
        print ''.join(i)
def gen4e6():
    for i in res4e6: 
        print ''.join(i)
def gen4e70():
    for i in res4e70: 
        print ''.join(i)
def gen4e71():
    for i in res4e71: 
        print ''.join(i)
def gen4e72():
    for i in res4e72: 
        print ''.join(i)
def gen4e73():
    for i in res4e73: 
        print ''.join(i)
def gen4e74():
    for i in res4e74: 
        print ''.join(i)
def gen4e75():
    for i in res4e75: 
        print ''.join(i)
def gen4e76():
    for i in res4e76: 
        print ''.join(i)
def gen4e77():
    for i in res4e77: 
        print ''.join(i)
def gen4e78():
    for i in res4e78: 
        print ''.join(i)
def gen4e79():
    for i in res4e79: 
        print ''.join(i)
def gen4e7():
    for i in res4e7: 
        print ''.join(i)
def gen4e8():
    for i in res4e8: 
        print ''.join(i)
def gen4e9():
    for i in res4e9: 
        print ''.join(i)
def gen4f10():
    for i in res4f10: 
        print ''.join(i)
def gen4f11():
    for i in res4f11: 
        print ''.join(i)
def gen4f12():
    for i in res4f12: 
        print ''.join(i)
def gen4f13():
    for i in res4f13: 
        print ''.join(i)
def gen4f14():
    for i in res4f14: 
        print ''.join(i)
def gen4f15():
    for i in res4f15: 
        print ''.join(i)
def gen4f16():
    for i in res4f16: 
        print ''.join(i)
def gen4f17():
    for i in res4f17: 
        print ''.join(i)
def gen4f18():
    for i in res4f18: 
        print ''.join(i)
def gen4f19():
    for i in res4f19: 
        print ''.join(i)
def gen4f1():
    for i in res4f1: 
        print ''.join(i)
def gen4f20():
    for i in res4f20: 
        print ''.join(i)
def gen4f21():
    for i in res4f21: 
        print ''.join(i)
def gen4f22():
    for i in res4f22: 
        print ''.join(i)
def gen4f23():
    for i in res4f23: 
        print ''.join(i)
def gen4f24():
    for i in res4f24: 
        print ''.join(i)
def gen4f25():
    for i in res4f25: 
        print ''.join(i)
def gen4f26():
    for i in res4f26: 
        print ''.join(i)
def gen4f27():
    for i in res4f27: 
        print ''.join(i)
def gen4f28():
    for i in res4f28: 
        print ''.join(i)
def gen4f29():
    for i in res4f29: 
        print ''.join(i)
def gen4f2():
    for i in res4f2: 
        print ''.join(i)
def gen4f30():
    for i in res4f30: 
        print ''.join(i)
def gen4f31():
    for i in res4f31: 
        print ''.join(i)
def gen4f32():
    for i in res4f32: 
        print ''.join(i)
def gen4f33():
    for i in res4f33: 
        print ''.join(i)
def gen4f34():
    for i in res4f34: 
        print ''.join(i)
def gen4f35():
    for i in res4f35: 
        print ''.join(i)
def gen4f36():
    for i in res4f36: 
        print ''.join(i)
def gen4f37():
    for i in res4f37: 
        print ''.join(i)
def gen4f38():
    for i in res4f38: 
        print ''.join(i)
def gen4f39():
    for i in res4f39: 
        print ''.join(i)
def gen4f3():
    for i in res4f3: 
        print ''.join(i)
def gen4f40():
    for i in res4f40: 
        print ''.join(i)
def gen4f41():
    for i in res4f41: 
        print ''.join(i)
def gen4f42():
    for i in res4f42: 
        print ''.join(i)
def gen4f43():
    for i in res4f43: 
        print ''.join(i)
def gen4f44():
    for i in res4f44: 
        print ''.join(i)
def gen4f45():
    for i in res4f45: 
        print ''.join(i)
def gen4f46():
    for i in res4f46: 
        print ''.join(i)
def gen4f47():
    for i in res4f47: 
        print ''.join(i)
def gen4f48():
    for i in res4f48: 
        print ''.join(i)
def gen4f49():
    for i in res4f49: 
        print ''.join(i)
def gen4f4():
    for i in res4f4: 
        print ''.join(i)
def gen4f50():
    for i in res4f50: 
        print ''.join(i)
def gen4f51():
    for i in res4f51: 
        print ''.join(i)
def gen4f52():
    for i in res4f52: 
        print ''.join(i)
def gen4f53():
    for i in res4f53: 
        print ''.join(i)
def gen4f54():
    for i in res4f54: 
        print ''.join(i)
def gen4f55():
    for i in res4f55: 
        print ''.join(i)
def gen4f56():
    for i in res4f56: 
        print ''.join(i)
def gen4f57():
    for i in res4f57: 
        print ''.join(i)
def gen4f58():
    for i in res4f58: 
        print ''.join(i)
def gen4f59():
    for i in res4f59: 
        print ''.join(i)
def gen4f5():
    for i in res4f5: 
        print ''.join(i)
def gen4f60():
    for i in res4f60: 
        print ''.join(i)
def gen4f61():
    for i in res4f61: 
        print ''.join(i)
def gen4f62():
    for i in res4f62: 
        print ''.join(i)
def gen4f63():
    for i in res4f63: 
        print ''.join(i)
def gen4f64():
    for i in res4f64: 
        print ''.join(i)
def gen4f65():
    for i in res4f65: 
        print ''.join(i)
def gen4f66():
    for i in res4f66: 
        print ''.join(i)
def gen4f67():
    for i in res4f67: 
        print ''.join(i)
def gen4f68():
    for i in res4f68: 
        print ''.join(i)
def gen4f69():
    for i in res4f69: 
        print ''.join(i)
def gen4f6():
    for i in res4f6: 
        print ''.join(i)
def gen4f70():
    for i in res4f70: 
        print ''.join(i)
def gen4f71():
    for i in res4f71: 
        print ''.join(i)
def gen4f72():
    for i in res4f72: 
        print ''.join(i)
def gen4f73():
    for i in res4f73: 
        print ''.join(i)
def gen4f74():
    for i in res4f74: 
        print ''.join(i)
def gen4f75():
    for i in res4f75: 
        print ''.join(i)
def gen4f76():
    for i in res4f76: 
        print ''.join(i)
def gen4f77():
    for i in res4f77: 
        print ''.join(i)
def gen4f78():
    for i in res4f78: 
        print ''.join(i)
def gen4f79():
    for i in res4f79: 
        print ''.join(i)
def gen4f7():
    for i in res4f7: 
        print ''.join(i)
def gen4f8():
    for i in res4f8: 
        print ''.join(i)
def gen4f9():
    for i in res4f9: 
        print ''.join(i)
def gen4g10():
    for i in res4g10: 
        print ''.join(i)
def gen4g11():
    for i in res4g11: 
        print ''.join(i)
def gen4g12():
    for i in res4g12: 
        print ''.join(i)
def gen4g13():
    for i in res4g13: 
        print ''.join(i)
def gen4g14():
    for i in res4g14: 
        print ''.join(i)
def gen4g15():
    for i in res4g15: 
        print ''.join(i)
def gen4g16():
    for i in res4g16: 
        print ''.join(i)
def gen4g17():
    for i in res4g17: 
        print ''.join(i)
def gen4g18():
    for i in res4g18: 
        print ''.join(i)
def gen4g19():
    for i in res4g19: 
        print ''.join(i)
def gen4g1():
    for i in res4g1: 
        print ''.join(i)
def gen4g20():
    for i in res4g20: 
        print ''.join(i)
def gen4g21():
    for i in res4g21: 
        print ''.join(i)
def gen4g22():
    for i in res4g22: 
        print ''.join(i)
def gen4g23():
    for i in res4g23: 
        print ''.join(i)
def gen4g24():
    for i in res4g24: 
        print ''.join(i)
def gen4g25():
    for i in res4g25: 
        print ''.join(i)
def gen4g26():
    for i in res4g26: 
        print ''.join(i)
def gen4g27():
    for i in res4g27: 
        print ''.join(i)
def gen4g28():
    for i in res4g28: 
        print ''.join(i)
def gen4g29():
    for i in res4g29: 
        print ''.join(i)
def gen4g2():
    for i in res4g2: 
        print ''.join(i)
def gen4g30():
    for i in res4g30: 
        print ''.join(i)
def gen4g31():
    for i in res4g31: 
        print ''.join(i)
def gen4g32():
    for i in res4g32: 
        print ''.join(i)
def gen4g33():
    for i in res4g33: 
        print ''.join(i)
def gen4g34():
    for i in res4g34: 
        print ''.join(i)
def gen4g35():
    for i in res4g35: 
        print ''.join(i)
def gen4g36():
    for i in res4g36: 
        print ''.join(i)
def gen4g37():
    for i in res4g37: 
        print ''.join(i)
def gen4g38():
    for i in res4g38: 
        print ''.join(i)
def gen4g39():
    for i in res4g39: 
        print ''.join(i)
def gen4g3():
    for i in res4g3: 
        print ''.join(i)
def gen4g40():
    for i in res4g40: 
        print ''.join(i)
def gen4g41():
    for i in res4g41: 
        print ''.join(i)
def gen4g42():
    for i in res4g42: 
        print ''.join(i)
def gen4g43():
    for i in res4g43: 
        print ''.join(i)
def gen4g44():
    for i in res4g44: 
        print ''.join(i)
def gen4g45():
    for i in res4g45: 
        print ''.join(i)
def gen4g46():
    for i in res4g46: 
        print ''.join(i)
def gen4g47():
    for i in res4g47: 
        print ''.join(i)
def gen4g48():
    for i in res4g48: 
        print ''.join(i)
def gen4g49():
    for i in res4g49: 
        print ''.join(i)
def gen4g4():
    for i in res4g4: 
        print ''.join(i)
def gen4g50():
    for i in res4g50: 
        print ''.join(i)
def gen4g51():
    for i in res4g51: 
        print ''.join(i)
def gen4g52():
    for i in res4g52: 
        print ''.join(i)
def gen4g53():
    for i in res4g53: 
        print ''.join(i)
def gen4g54():
    for i in res4g54: 
        print ''.join(i)
def gen4g55():
    for i in res4g55: 
        print ''.join(i)
def gen4g56():
    for i in res4g56: 
        print ''.join(i)
def gen4g57():
    for i in res4g57: 
        print ''.join(i)
def gen4g58():
    for i in res4g58: 
        print ''.join(i)
def gen4g59():
    for i in res4g59: 
        print ''.join(i)
def gen4g5():
    for i in res4g5: 
        print ''.join(i)
def gen4g60():
    for i in res4g60: 
        print ''.join(i)
def gen4g61():
    for i in res4g61: 
        print ''.join(i)
def gen4g62():
    for i in res4g62: 
        print ''.join(i)
def gen4g63():
    for i in res4g63: 
        print ''.join(i)
def gen4g64():
    for i in res4g64: 
        print ''.join(i)
def gen4g65():
    for i in res4g65: 
        print ''.join(i)
def gen4g66():
    for i in res4g66: 
        print ''.join(i)
def gen4g67():
    for i in res4g67: 
        print ''.join(i)
def gen4g68():
    for i in res4g68: 
        print ''.join(i)
def gen4g69():
    for i in res4g69: 
        print ''.join(i)
def gen4g6():
    for i in res4g6: 
        print ''.join(i)
def gen4g70():
    for i in res4g70: 
        print ''.join(i)
def gen4g71():
    for i in res4g71: 
        print ''.join(i)
def gen4g72():
    for i in res4g72: 
        print ''.join(i)
def gen4g73():
    for i in res4g73: 
        print ''.join(i)
def gen4g74():
    for i in res4g74: 
        print ''.join(i)
def gen4g75():
    for i in res4g75: 
        print ''.join(i)
def gen4g76():
    for i in res4g76: 
        print ''.join(i)
def gen4g77():
    for i in res4g77: 
        print ''.join(i)
def gen4g78():
    for i in res4g78: 
        print ''.join(i)
def gen4g79():
    for i in res4g79: 
        print ''.join(i)
def gen4g7():
    for i in res4g7: 
        print ''.join(i)
def gen4g8():
    for i in res4g8: 
        print ''.join(i)
def gen4g9():
    for i in res4g9: 
        print ''.join(i)
def gen4h10():
    for i in res4h10: 
        print ''.join(i)
def gen4h11():
    for i in res4h11: 
        print ''.join(i)
def gen4h12():
    for i in res4h12: 
        print ''.join(i)
def gen4h13():
    for i in res4h13: 
        print ''.join(i)
def gen4h14():
    for i in res4h14: 
        print ''.join(i)
def gen4h15():
    for i in res4h15: 
        print ''.join(i)
def gen4h16():
    for i in res4h16: 
        print ''.join(i)
def gen4h17():
    for i in res4h17: 
        print ''.join(i)
def gen4h18():
    for i in res4h18: 
        print ''.join(i)
def gen4h19():
    for i in res4h19: 
        print ''.join(i)
def gen4h1():
    for i in res4h1: 
        print ''.join(i)
def gen4h20():
    for i in res4h20: 
        print ''.join(i)
def gen4h21():
    for i in res4h21: 
        print ''.join(i)
def gen4h22():
    for i in res4h22: 
        print ''.join(i)
def gen4h23():
    for i in res4h23: 
        print ''.join(i)
def gen4h24():
    for i in res4h24: 
        print ''.join(i)
def gen4h25():
    for i in res4h25: 
        print ''.join(i)
def gen4h26():
    for i in res4h26: 
        print ''.join(i)
def gen4h27():
    for i in res4h27: 
        print ''.join(i)
def gen4h28():
    for i in res4h28: 
        print ''.join(i)
def gen4h29():
    for i in res4h29: 
        print ''.join(i)
def gen4h2():
    for i in res4h2: 
        print ''.join(i)
def gen4h30():
    for i in res4h30: 
        print ''.join(i)
def gen4h31():
    for i in res4h31: 
        print ''.join(i)
def gen4h32():
    for i in res4h32: 
        print ''.join(i)
def gen4h33():
    for i in res4h33: 
        print ''.join(i)
def gen4h34():
    for i in res4h34: 
        print ''.join(i)
def gen4h35():
    for i in res4h35: 
        print ''.join(i)
def gen4h36():
    for i in res4h36: 
        print ''.join(i)
def gen4h37():
    for i in res4h37: 
        print ''.join(i)
def gen4h38():
    for i in res4h38: 
        print ''.join(i)
def gen4h39():
    for i in res4h39: 
        print ''.join(i)
def gen4h3():
    for i in res4h3: 
        print ''.join(i)
def gen4h40():
    for i in res4h40: 
        print ''.join(i)
def gen4h41():
    for i in res4h41: 
        print ''.join(i)
def gen4h42():
    for i in res4h42: 
        print ''.join(i)
def gen4h43():
    for i in res4h43: 
        print ''.join(i)
def gen4h44():
    for i in res4h44: 
        print ''.join(i)
def gen4h45():
    for i in res4h45: 
        print ''.join(i)
def gen4h46():
    for i in res4h46: 
        print ''.join(i)
def gen4h47():
    for i in res4h47: 
        print ''.join(i)
def gen4h48():
    for i in res4h48: 
        print ''.join(i)
def gen4h49():
    for i in res4h49: 
        print ''.join(i)
def gen4h4():
    for i in res4h4: 
        print ''.join(i)
def gen4h50():
    for i in res4h50: 
        print ''.join(i)
def gen4h51():
    for i in res4h51: 
        print ''.join(i)
def gen4h52():
    for i in res4h52: 
        print ''.join(i)
def gen4h53():
    for i in res4h53: 
        print ''.join(i)
def gen4h54():
    for i in res4h54: 
        print ''.join(i)
def gen4h55():
    for i in res4h55: 
        print ''.join(i)
def gen4h56():
    for i in res4h56: 
        print ''.join(i)
def gen4h57():
    for i in res4h57: 
        print ''.join(i)
def gen4h58():
    for i in res4h58: 
        print ''.join(i)
def gen4h59():
    for i in res4h59: 
        print ''.join(i)
def gen4h5():
    for i in res4h5: 
        print ''.join(i)
def gen4h60():
    for i in res4h60: 
        print ''.join(i)
def gen4h61():
    for i in res4h61: 
        print ''.join(i)
def gen4h62():
    for i in res4h62: 
        print ''.join(i)
def gen4h63():
    for i in res4h63: 
        print ''.join(i)
def gen4h64():
    for i in res4h64: 
        print ''.join(i)
def gen4h65():
    for i in res4h65: 
        print ''.join(i)
def gen4h66():
    for i in res4h66: 
        print ''.join(i)
def gen4h67():
    for i in res4h67: 
        print ''.join(i)
def gen4h68():
    for i in res4h68: 
        print ''.join(i)
def gen4h69():
    for i in res4h69: 
        print ''.join(i)
def gen4h6():
    for i in res4h6: 
        print ''.join(i)
def gen4h70():
    for i in res4h70: 
        print ''.join(i)
def gen4h71():
    for i in res4h71: 
        print ''.join(i)
def gen4h72():
    for i in res4h72: 
        print ''.join(i)
def gen4h73():
    for i in res4h73: 
        print ''.join(i)
def gen4h74():
    for i in res4h74: 
        print ''.join(i)
def gen4h75():
    for i in res4h75: 
        print ''.join(i)
def gen4h76():
    for i in res4h76: 
        print ''.join(i)
def gen4h77():
    for i in res4h77: 
        print ''.join(i)
def gen4h78():
    for i in res4h78: 
        print ''.join(i)
def gen4h79():
    for i in res4h79: 
        print ''.join(i)
def gen4h7():
    for i in res4h7: 
        print ''.join(i)
def gen4h8():
    for i in res4h8: 
        print ''.join(i)
def gen4h9():
    for i in res4h9: 
        print ''.join(i)
def gen4i10():
    for i in res4i10: 
        print ''.join(i)
def gen4i11():
    for i in res4i11: 
        print ''.join(i)
def gen4i12():
    for i in res4i12: 
        print ''.join(i)
def gen4i13():
    for i in res4i13: 
        print ''.join(i)
def gen4i14():
    for i in res4i14: 
        print ''.join(i)
def gen4i15():
    for i in res4i15: 
        print ''.join(i)
def gen4i16():
    for i in res4i16: 
        print ''.join(i)
def gen4i17():
    for i in res4i17: 
        print ''.join(i)
def gen4i18():
    for i in res4i18: 
        print ''.join(i)
def gen4i19():
    for i in res4i19: 
        print ''.join(i)
def gen4i1():
    for i in res4i1: 
        print ''.join(i)
def gen4i20():
    for i in res4i20: 
        print ''.join(i)
def gen4i21():
    for i in res4i21: 
        print ''.join(i)
def gen4i22():
    for i in res4i22: 
        print ''.join(i)
def gen4i23():
    for i in res4i23: 
        print ''.join(i)
def gen4i24():
    for i in res4i24: 
        print ''.join(i)
def gen4i25():
    for i in res4i25: 
        print ''.join(i)
def gen4i26():
    for i in res4i26: 
        print ''.join(i)
def gen4i27():
    for i in res4i27: 
        print ''.join(i)
def gen4i28():
    for i in res4i28: 
        print ''.join(i)
def gen4i29():
    for i in res4i29: 
        print ''.join(i)
def gen4i2():
    for i in res4i2: 
        print ''.join(i)
def gen4i30():
    for i in res4i30: 
        print ''.join(i)
def gen4i31():
    for i in res4i31: 
        print ''.join(i)
def gen4i32():
    for i in res4i32: 
        print ''.join(i)
def gen4i33():
    for i in res4i33: 
        print ''.join(i)
def gen4i34():
    for i in res4i34: 
        print ''.join(i)
def gen4i35():
    for i in res4i35: 
        print ''.join(i)
def gen4i36():
    for i in res4i36: 
        print ''.join(i)
def gen4i37():
    for i in res4i37: 
        print ''.join(i)
def gen4i38():
    for i in res4i38: 
        print ''.join(i)
def gen4i39():
    for i in res4i39: 
        print ''.join(i)
def gen4i3():
    for i in res4i3: 
        print ''.join(i)
def gen4i40():
    for i in res4i40: 
        print ''.join(i)
def gen4i41():
    for i in res4i41: 
        print ''.join(i)
def gen4i42():
    for i in res4i42: 
        print ''.join(i)
def gen4i43():
    for i in res4i43: 
        print ''.join(i)
def gen4i44():
    for i in res4i44: 
        print ''.join(i)
def gen4i45():
    for i in res4i45: 
        print ''.join(i)
def gen4i46():
    for i in res4i46: 
        print ''.join(i)
def gen4i47():
    for i in res4i47: 
        print ''.join(i)
def gen4i48():
    for i in res4i48: 
        print ''.join(i)
def gen4i49():
    for i in res4i49: 
        print ''.join(i)
def gen4i4():
    for i in res4i4: 
        print ''.join(i)
def gen4i50():
    for i in res4i50: 
        print ''.join(i)
def gen4i51():
    for i in res4i51: 
        print ''.join(i)
def gen4i52():
    for i in res4i52: 
        print ''.join(i)
def gen4i53():
    for i in res4i53: 
        print ''.join(i)
def gen4i54():
    for i in res4i54: 
        print ''.join(i)
def gen4i55():
    for i in res4i55: 
        print ''.join(i)
def gen4i56():
    for i in res4i56: 
        print ''.join(i)
def gen4i57():
    for i in res4i57: 
        print ''.join(i)
def gen4i58():
    for i in res4i58: 
        print ''.join(i)
def gen4i59():
    for i in res4i59: 
        print ''.join(i)
def gen4i5():
    for i in res4i5: 
        print ''.join(i)
def gen4i60():
    for i in res4i60: 
        print ''.join(i)
def gen4i61():
    for i in res4i61: 
        print ''.join(i)
def gen4i62():
    for i in res4i62: 
        print ''.join(i)
def gen4i63():
    for i in res4i63: 
        print ''.join(i)
def gen4i64():
    for i in res4i64: 
        print ''.join(i)
def gen4i65():
    for i in res4i65: 
        print ''.join(i)
def gen4i66():
    for i in res4i66: 
        print ''.join(i)
def gen4i67():
    for i in res4i67: 
        print ''.join(i)
def gen4i68():
    for i in res4i68: 
        print ''.join(i)
def gen4i69():
    for i in res4i69: 
        print ''.join(i)
def gen4i6():
    for i in res4i6: 
        print ''.join(i)
def gen4i70():
    for i in res4i70: 
        print ''.join(i)
def gen4i71():
    for i in res4i71: 
        print ''.join(i)
def gen4i72():
    for i in res4i72: 
        print ''.join(i)
def gen4i73():
    for i in res4i73: 
        print ''.join(i)
def gen4i74():
    for i in res4i74: 
        print ''.join(i)
def gen4i75():
    for i in res4i75: 
        print ''.join(i)
def gen4i76():
    for i in res4i76: 
        print ''.join(i)
def gen4i77():
    for i in res4i77: 
        print ''.join(i)
def gen4i78():
    for i in res4i78: 
        print ''.join(i)
def gen4i79():
    for i in res4i79: 
        print ''.join(i)
def gen4i7():
    for i in res4i7: 
        print ''.join(i)
def gen4i8():
    for i in res4i8: 
        print ''.join(i)
def gen4i9():
    for i in res4i9: 
        print ''.join(i)
