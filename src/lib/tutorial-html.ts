export function prepareTutorialHtml(html: string): string {
  return html
    .replace(/<a href="#objectives">Objectives<\/a>/g, '')
    .replace(/<section class="tutorial-section tutorial-objectives" id="objectives">[\s\S]*?<\/section>/g, '')
    .replace(
      '<span class="stat-chip"><strong>EN/BN</strong> bilingual</span>',
      '<span class="stat-chip"><strong>Practice</strong> built in</span>',
    )
    .replace(
      '<span><strong>EN/BN</strong> bilingual</span>',
      '<span><strong>English</strong> tutorial</span>',
    );
}
