import { render, screen } from '@testing-library/react';
import { describe, expect, it } from 'vitest';
import OfflinePage from '@/app/offline/page';

describe('OfflinePage', () => {
  it('renders a usable recovery path', () => {
    render(<OfflinePage />);

    expect(screen.getByRole('heading', { name: 'You are currently offline.' })).toBeInTheDocument();
    expect(screen.getByRole('link', { name: 'Reconnect and return home' })).toHaveAttribute('href', '/');
    expect(screen.getByRole('link', { name: 'Open cached tutorials' })).toHaveAttribute('href', '/tutorials/');
  });
});
