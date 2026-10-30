import copy,unittest
import notification_style as n
class StyleTests(unittest.TestCase):
    def entry(self):return {'title':'Coin Tarama5 V3 · GERİ TEST — GİRİŞ TEYİDİ','body':'@name\n\n**GERİ TEST — GİRİŞ TEYİDİ · FOGO · OKX PERP**\nFiyat1\n<!-- coin-tarama-5-v3:abc -->'}
    def test_real_entry_title_and_body(self):
        p=n.style(self.entry());self.assertTrue(p['title'].startswith(n.ENTRY));self.assertIn('**🟢🎯 GERİ TEST',p['body']);self.assertIn('> 🟢🎯 **GİRİŞ TEYİDİ**',p['body'])
    def test_negative_entry_text_not_highlighted(self):
        p={'title':'ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL','body':'**ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL · COIN**\nHenüz giriş teyidi yok.'};self.assertEqual(n.style(p),p)
    def test_cancelled_only_not_highlighted(self):
        p={'title':'İPTAL','body':'**İPTAL · FOGO**'};self.assertEqual(n.style(p),p)
    def test_mixed_batch_marks_only_confirmed_row(self):
        p=self.entry();p['body']+='\n\n**ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL · OTHER**';r=n.style(p);self.assertIn('**ERKEN RADAR',r['body']);self.assertNotIn('🟢🎯 ERKEN',r['body'])
    def test_meme_technical_confirmation_keeps_its_meaning(self):
        p={'title':'Coin Tarama Meme','body':'SPSC · solana · 15 dk fiyat teyidi + 5 dk alım akışı · accumulation\n```text\nExactCA\n```'};r=n.style(p);self.assertTrue(r['title'].startswith(n.TECHNICAL));self.assertNotIn(n.ENTRY,r['body']);self.assertIn('ExactCA',r['body'])
    def test_meme_early_does_not_become_confirmation(self):
        p={'title':'Coin Tarama Meme','body':'SPSC · solana · 5 dk ilk taban + alım yönlü hacim · accumulation'};self.assertEqual(n.style(p),p)
    def test_actual_swap_is_not_entry_confirmation(self):
        p={'title':'1 coin','body':'**ALIM**\nGerçek swap, giriş teyidi değil.'};self.assertEqual(n.style(p),p)
    def test_repeat_is_idempotent(self):
        p=n.style(self.entry());self.assertEqual(n.style(p),p)
    def test_markers_and_numbers_unchanged(self):
        p=self.entry();p['body']+='\nStop0.002739461084131215\n```text\nExactCA\n```';r=n.style(p);self.assertIn('<!-- coin-tarama-5-v3:abc -->',r['body']);self.assertIn('Stop0.002739461084131215',r['body']);self.assertIn('```text\nExactCA\n```',r['body'])
    def test_no_input_mutation(self):
        p=self.entry();before=copy.deepcopy(p);n.style(p);self.assertEqual(before,p)
    def test_no_changes_to_other_api_or_telegram(self):
        p=self.entry()
        for url in ['https://api.telegram.org/bot123/sendMessage','https://api.github.com/repos/other/repo/issues','https://api.github.com/repos/selvisezgin01-ux/Coin-Tarama/actions/runs']:self.assertIs(n.outgoing(url,p),p)
    def test_known_fixed_issue_endpoint(self):self.assertTrue(n.outgoing('https://api.github.com/repos/selvisezgin01-ux/Coin-Tarama/issues',self.entry())['title'].startswith(n.ENTRY))
    def test_code_block_text_cannot_change_stage(self):
        p={'title':'test','body':'```\n**GERİ TEST — GİRİŞ TEYİDİ · FAKE**\n```'};self.assertEqual(n.style(p),p)
    def test_test_notification_not_promoted(self):
        p=self.entry();p['title']='TEST · Gerçek sinyal değil';self.assertEqual(n.style(p),p)
if __name__=='__main__':unittest.main()
