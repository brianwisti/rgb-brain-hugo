#!/usr/bin/env perl

use 5.38.0;
use warnings;

use Cwd 'getcwd';

use Data::Dumper qw(Dumper);
use Mojo::File;
use Mojo::JSON qw(encode_json);
use Mojo::Util 'url_unescape';
use Path::Tiny;
use Try::Tiny;

my $CONTENT_DIR = "content";
my $NOTE_LINK = qr{
  \[
    (?<title> [^\]]+? )
  \]
  \(
    (?<path> [^\)]+? \.md)
  \)
}xm;

sub find_backlinks_in_content() {
  my $root = getcwd();

  my $backlinks_to = {};
  my $content_dir = Mojo::File->new( $CONTENT_DIR )->realpath;
  # my $output = url_escape( $input );
  my $notes = $content_dir->list_tree->grep(sub { $_->extname eq "md" });

  $notes->each(sub($note, $index) {
    my $content = $note->slurp;
    my $content_path = $note->to_rel( $content_dir );
    say "$index: $note ($content_path)";

    while ( $content =~ m/$NOTE_LINK/g ) {
      my $link_title = $+{title};
      my $link_path = url_unescape( $+{path} );

      next if $link_path =~ /^https?:/;

      # TODO: Figure out how to say this with Mojo::File maybe
      try {
        my $content_link_path = Path::Tiny::path($link_path)->absolute($note->dirname)->realpath->relative("$root/content") . "";
        say "\t$link_title -> $link_path -> $content_link_path";

        unless ( $backlinks_to->{ $content_link_path } ) {
          $backlinks_to->{ $content_link_path } = [];
        }

        push $backlinks_to->{$content_link_path}->@*, { title => $note->basename(".md"), path => "$content_path" };
      } catch {
        die "LINK ERROR: $note -> $link_path";
      };
    }
  });

  return $backlinks_to;
}

sub main {
  my $backlinks = find_backlinks_in_content();
  my $as_json = encode_json( $backlinks );
  Mojo::File->new("data/backlinks.json")->spew( $as_json );
}

main();
