# Load the Module::Install bundled in ./inc/
use lib '.'; # added since from Perl 5.26 '.' is no more in @INC
use inc::Module::Install;

##############################################################################
# Define metadata (we read it from the binary)

name              'check_free_mem';
version_from      'check_free_mem';
perl_version_from 'check_free_mem';
all_from          'check_free_mem.pod';

##############################################################################
# Specific dependencies

include 'version';

my %prereqs = (
    'Carp'                          => 0,
    'English'                       => 0,
    'File::Slurp'                   => 0,
    'Getopt::Long'                  => 0,
    'Monitoring::Plugin'            => 0,
    'Monitoring::Plugin::Getopt'    => 0,
    'Monitoring::Plugin::Threshold' => 0,
    'Readonly'                      => 0,
    'version'                       => 0,
);

install_script  'check_free_mem';

WriteMakefile(
    PREREQ_PM            => \%prereqs,
    INSTALLSCRIPT        => '/usr/lib/nagios/plugins/contrib',
    INSTALLSITESCRIPT    => '/usr/lib/nagios/plugins/contrib',
    MAN1PODS             => { 'check_free_mem.pod' => 'blib/man1/check_free_mem.1', },
    MAN3PODS             => { },
);
