import { describe, expect, it } from 'vitest';
import { prepareTutorialHtml } from '@/src/lib/tutorial-html';

describe('prepareTutorialHtml', () => {
  it('removes the generic objective card and Objectives jump link', () => {
    const html = `
      <nav class="chapter-jump">
        <a href="#objectives">Objectives</a>
        <a href="#concept-1">Learn</a>
      </nav>
      <section class="tutorial-section tutorial-objectives" id="objectives">
        <div class="section-kicker">Start here</div>
        <h2>What you will learn</h2>
      </section>
      <section id="concept-1"><h2>Observations</h2></section>
    `;

    const result = prepareTutorialHtml(html);

    expect(result).not.toContain('href="#objectives"');
    expect(result).not.toContain('tutorial-objectives');
    expect(result).not.toContain('What you will learn');
    expect(result).toContain('Observations');
  });

  it('relabels old bilingual course statistics without deleting teaching content', () => {
    const html =
      '<span class="stat-chip"><strong>EN/BN</strong> bilingual</span><article>Keep this lesson</article>';

    const result = prepareTutorialHtml(html);

    expect(result).toContain('<strong>Practice</strong> built in');
    expect(result).toContain('Keep this lesson');
  });
});
